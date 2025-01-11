import os
from typing import List

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

import torch
import cohere
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification, 
    pipeline
)

app = FastAPI()

# Allow requests from a different port (Streamlit)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Folder for uploaded files
UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Cohere Setup
# Manually provide the Cohere API key
COHERE_API_KEY = "ZvWNnq87BJPfEmegG3zunSB65dzSF1ZL28TXM6gI"  # Replace with your actual Cohere API key
co = cohere.Client(COHERE_API_KEY)


def summarize_with_cohere(text: str) -> str:
    """
    Summarize large transcripts using Cohere.
    We'll aim for a 'long' summary to preserve detail.
    """
    if not COHERE_API_KEY or COHERE_API_KEY == "YOUR_COHERE_API_KEY":
        return "(Error: No valid Cohere API key. Returning original text.)\n" + text

    try:
        response = co.summarize(
            text=text,
            length="long",      # more detailed
            format="paragraph", 
            extractiveness="auto", 
            temperature=0.3
        )
        return response.summary
    except Exception as e:
        return f"(Cohere Summarization Error: {e})\n{text}"

# Local DistilBERT for sentiment
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    local_sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model=model,
        tokenizer=tokenizer,
        device=torch.device("cpu"),
        truncation=True,
        max_length=512
    )
except Exception as e:
    print("Error loading DistilBERT pipeline:", e)
    local_sentiment_pipeline = None

@app.get("/")
def home():
    return {"message": "Cohere Summarize + DistilBERT Sentiment API (Enhanced)"}

@app.post("/analyze")
async def analyze_files(
    files: List[UploadFile] = File(...),
    threshold: float = Form(...)
):
    """
    1) Summarize each transcript with Cohere (long format).
    2) Run DistilBERT sentiment on the entire summary (no snippet).
    3) If top confidence < threshold => label=NEUTRAL.
    4) Return JSON with full summary and results.
    """
    results = []
    for file in files:
        content = await file.read()

        # Optionally save
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(content)

        original_text = content.decode("utf-8", errors="replace")

        # Summarize
        summary = summarize_with_cohere(original_text)

        if not local_sentiment_pipeline:
            results.append({
                "filename": file.filename,
                "error": "DistilBERT pipeline not loaded."
            })
            continue

        try:
            sentiment_result = local_sentiment_pipeline(summary)
            if not sentiment_result:
                results.append({
                    "filename": file.filename,
                    "error": "Empty sentiment result"
                })
                continue

            top_label = sentiment_result[0]["label"].upper()  # POSITIVE or NEGATIVE
            top_score = sentiment_result[0]["score"]

            final_label = top_label
            if top_score < threshold:
                final_label = "NEUTRAL"

            results.append({
                "filename": file.filename,
                "summary": summary,
                "sentiment_label": final_label,
                "confidence": top_score
            })

        except Exception as ex:
            results.append({
                "filename": file.filename,
                "error": str(ex)
            })

    return {
        "message": f"Analyzed {len(files)} file(s) with threshold={threshold}.",
        "results": results
    }