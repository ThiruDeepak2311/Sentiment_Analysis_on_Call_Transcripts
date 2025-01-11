# Sentiment Analysis on Call Transcripts

This project is a **Sentiment Analysis and Summarization Tool** for call transcripts using **Streamlit** as the frontend and powerful NLP models for backend processing. Users can upload transcript files, view summarized content, analyze sentiment, and visualize the results interactively.

---

[https://github.com/ThiruDeepak2311/Sentiment_Analysis_on_Call_Transcripts/issues/1#issue-2781683006](https://private-user-images.githubusercontent.com/116452492/402230972-5bbe50ba-5e4f-4648-a8d8-4c4e98a5324d.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzY1ODE0MzcsIm5iZiI6MTczNjU4MTEzNywicGF0aCI6Ii8xMTY0NTI0OTIvNDAyMjMwOTcyLTViYmU1MGJhLTVlNGYtNDY0OC1hOGQ4LTRjNGU5OGE1MzI0ZC5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTExJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDExMVQwNzM4NTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hYWZkZDA2NDU2ZTlhYTI3ZjQzYTg5MzVkMmMwYTdjNTUxNTg1NjlkMDgyYzEyOTQxMjY4NmQwN2ZlNjJhNWI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.BY1LsX_xCoSkdjOo7Y00VKEvZUaGLx17YT3hl3OjqIA)

---

## Features

1. **User Authentication**: Secure login for users before accessing the app.
2. **File Upload**: Upload one or more `.txt` files for analysis.
3. **Summarization**: Cohere API for summarizing the content of the transcripts.
4. **Sentiment Analysis**: DistilBERT or an equivalent model for generating sentiment labels (Positive, Neutral, Negative).
5. **Interactive Display**:
    - Summarized results in a neat table format.
6. **Visualizations**:
    - Pie chart for sentiment distribution.
    - Histogram for confidence score distribution.
7. **Professional UI**: Clean, responsive, and professional interface for ease of use.
8. **Error Handling**: Displays clear error messages if processing fails.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher installed on your system.
- Virtual environment for managing dependencies (optional but recommended).
- Hugging Face and Cohere API keys (if required).

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sentiment_analysis_on_call_transcripts
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your API keys (if required):
   Create a `.env` file in the root directory and add:
   ```
   COHERE_API_KEY=<your_cohere_api_key>
   HF_API_KEY=<your_hugging_face_api_key>
   ```

---

## Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser:
   The terminal will display a local URL (e.g., `http://localhost:8501`). Click on the link or copy-paste it into your browser.

3. Log in using the default credentials:
   ```
   Username: admin
   Password: 1234
   ```

4. Upload `.txt` files and start analyzing.

---

## File Structure

```plaintext
.
├── app.py                 # Streamlit frontend logic
├── main.py                # Backend API logic
├── requirements.txt       # Python dependencies
├── sample_files/          # Sample text files for testing
├── README.md              # Documentation (this file)
└── .gitignore             # Ignored files for Git
```

---

## Features Breakdown

### 1. Authentication
- Protects the application from unauthorized access.
- Users must log in to access any functionality.

### 2. File Upload and Analysis
- Supports uploading multiple `.txt` files.
- Processes each file to generate:
  - **Summary** (using Cohere API).
  - **Sentiment Label** (using DistilBERT or equivalent model).
  - **Confidence Score**.

### 3. Results Display
- Displays results in a **responsive table** with the following columns:
  - Filename
  - Summary Snippet
  - Sentiment Label
  - Confidence Score
  - Errors (if any)
- Full summaries can be viewed in a popup modal.

### 4. Visualizations
- **Pie Chart**: Distribution of sentiment labels.
- **Histogram**: Confidence scores of the predictions.

---

## Example Usage

1. **Upload Files**:
   - Drag and drop `.txt` files into the upload box.

2. **View Results**:
   - Analyze sentiment and summaries for all uploaded files.
   - Click `View Summary` to open a modal with the full summary.

3. **Visualizations**:
   - Sentiment label distribution.
   - Confidence score distribution.

---

## API Integration

### Cohere API (Summarization)
- Make sure you have a Cohere API key.
- Add the key to your `.env` file.

### Hugging Face (Sentiment Analysis)
- Uses Hugging Face Transformers for running sentiment analysis.
- Ensure the `requirements.txt` lists the required packages.

---

## Troubleshooting

1. **Missing Dependencies**:
   - Run `pip install -r requirements.txt`.

2. **Port Already in Use**:
   - Specify a different port: `streamlit run app.py --server.port=8502`.

3. **API Key Errors**:
   - Check the `.env` file for correct keys.

---

## Future Enhancements

1. Add support for additional file formats (e.g., PDFs).
2. Integrate more robust models for multilingual sentiment analysis.
3. Enhance the UI/UX with advanced design frameworks.

---

