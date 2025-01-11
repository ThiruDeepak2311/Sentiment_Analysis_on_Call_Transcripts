# Sentiment Analysis on Call Transcripts

This project is a **Sentiment Analysis and Summarization Tool** for call transcripts using **Streamlit** as the frontend and powerful NLP models for backend processing. Users can upload transcript files, view summarized content, analyze sentiment, and visualize the results interactively.

---

[https://github.com/ThiruDeepak2311/Sentiment_Analysis_on_Call_Transcripts/issues/1#issue-2781683006](https://private-user-images.githubusercontent.com/116452492/402230972-5bbe50ba-5e4f-4648-a8d8-4c4e98a5324d.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzY1ODE0MzcsIm5iZiI6MTczNjU4MTEzNywicGF0aCI6Ii8xMTY0NTI0OTIvNDAyMjMwOTcyLTViYmU1MGJhLTVlNGYtNDY0OC1hOGQ4LTRjNGU5OGE1MzI0ZC5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTExJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDExMVQwNzM4NTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hYWZkZDA2NDU2ZTlhYTI3ZjQzYTg5MzVkMmMwYTdjNTUxNTg1NjlkMDgyYzEyOTQxMjY4NmQwN2ZlNjJhNWI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.BY1LsX_xCoSkdjOo7Y00VKEvZUaGLx17YT3hl3OjqIA)

---

## 🌟 Features

- **Secure Authentication**
  - Login-protected dashboard
  - User session management
  - Secure credential validation

- **File Processing**
  - Multiple text file upload support
  - Batch processing capabilities
  - Progress tracking during analysis

- **Advanced Analysis**
  - Sentiment analysis using DistilBERT
  - Text summarization using Cohere API
  - Confidence scoring for sentiment predictions
  - Customizable confidence threshold

- **Rich Visualizations**
  - Interactive sentiment distribution pie charts
  - Confidence score histograms
  - Timeline analysis graphs
  - Real-time metrics dashboard

- **Modern UI/UX**
  - Dark theme interface
  - Responsive design
  - Interactive data tables
  - Loading states and error handling

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **ML Models**: 
  - DistilBERT (Sentiment Analysis)
  - Cohere API (Text Summarization)
- **Data Visualization**: Plotly Express
- **Styling**: Custom CSS with dark theme

## 📋 Prerequisites

```bash
# Required Python version
Python 3.8+

# Required Libraries
streamlit
fastapi
torch
transformers
cohere
plotly
pandas
python-multipart
uvicorn
```

## 🚀 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/call-transcript-analysis.git
cd call-transcript-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file
COHERE_API_KEY=your_cohere_api_key
```

4. Run the application:
```bash
# Terminal 1 - Start Backend
uvicorn backend:app --reload --port 8000

# Terminal 2 - Start Frontend
streamlit run frontend.py
```

## 💻 Usage

1. Access the application at `http://localhost:8501`
2. Login using the following credentials:
   - Username: `admin`
   - Password: `1234`
3. Upload text files containing call transcripts
4. Adjust the confidence threshold if needed
5. Click "Analyze Files" to process the transcripts
6. View the results in the interactive dashboard

## 📊 Analysis Features

The application provides comprehensive analysis including:

- Sentiment Classification (Positive/Negative/Neutral)
- Confidence Scores for Predictions
- Text Summarization
- Visual Analytics:
  - Sentiment Distribution
  - Confidence Score Distribution
  - Timeline Analysis

## 🔐 Security Features

- Password-protected access
- Session management
- Secure file handling
- Error handling and input validation

----

## 🙏 Acknowledgments

- Hugging Face for DistilBERT model
- Cohere for text summarization API
- Streamlit for the amazing web framework
- FastAPI for the efficient backend framework
----
