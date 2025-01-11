import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Hardcoded credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

# Complete styling with enhanced visuals (script related to summary removed)
STYLES = """
<style>
    body {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .stApp {
        background-color: #1a1a1a;
    }
    .main {
        background-color: #1a1a1a;
    }
    h1, h2, h3 {
        color: #ffffff !important;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #2d2d2d;
        color: white;
        border: 1px solid #404040;
        padding: 0.5rem 1rem;
        margin: 0.5rem 0;
        border-radius: 4px;
    }
    .stButton>button:hover {
        background-color: #404040;
        border-color: #505050;
    }
    .styled-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 1.5rem 0;
        background-color: #2d2d2d;
        border-radius: 8px;
        overflow: hidden;
    }
    .styled-table th {
        background-color: #1e3a5f;
        color: #ffffff;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    .styled-table td {
        padding: 12px;
        border-top: 1px solid #404040;
        color: #ffffff;
    }
    .styled-table tr:hover {
        background-color: #363636;
    }
    .metric-container {
        display: flex;
        justify-content: space-between;
        margin: 1rem 0;
        flex-wrap: wrap;
        gap: 1rem;
    }
    .metric-card {
        background-color: #1e3a5f;
        padding: 1.5rem;
        border-radius: 8px;
        flex: 1;
        min-width: 200px;
        text-align: center;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
</style>
"""

def show_login():
    st.markdown(STYLES, unsafe_allow_html=True)
    
    st.title("🔐 Text Analysis Dashboard")
    
    with st.container():
        st.markdown("### Welcome! Please login to continue")
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.button("Login"):
                if username == VALID_USERNAME and password == VALID_PASSWORD:
                    st.session_state["logged_in"] = True
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid credentials. Please try again.")

def create_metrics_dashboard(valid_df):
    st.markdown("""
    <div class="metric-container">
        <div class="metric-card">
            <div class="metric-label">Total Files</div>
            <div class="metric-value">{}</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Positive Sentiment</div>
            <div class="metric-value">{:.1f}%</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Average Confidence</div>
            <div class="metric-value">{:.1f}%</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Highest Confidence</div>
            <div class="metric-value">{:.1f}%</div>
        </div>
    </div>
    """.format(
        len(valid_df),
        (valid_df["sentiment_label"] == "POSITIVE").mean() * 100,
        valid_df["confidence"].mean() * 100,
        valid_df["confidence"].max() * 100
    ), unsafe_allow_html=True)

def create_visualizations(valid_df):
    st.markdown("### 📊 Analysis Visualizations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_sentiment = px.pie(
            valid_df,
            names="sentiment_label",
            title="Sentiment Distribution",
            color_discrete_sequence=["#4CAF50", "#f44336"],
            hole=0.4
        )
        fig_sentiment.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )
        st.plotly_chart(fig_sentiment, use_container_width=True)
    
    with col2:
        fig_conf = px.histogram(
            valid_df,
            x="confidence",
            color="sentiment_label",
            title="Confidence Distribution",
            color_discrete_sequence=["#4CAF50", "#f44336"]
        )
        fig_conf.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )
        st.plotly_chart(fig_conf, use_container_width=True)
    
    fig_timeline = px.line(
        valid_df,
        x=valid_df.index,
        y="confidence",
        color="sentiment_label",
        title="Confidence Timeline",
        color_discrete_sequence=["#4CAF50", "#f44336"]
    )
    fig_timeline.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis_title="File Number",
        yaxis_title="Confidence Score"
    )
    st.plotly_chart(fig_timeline, use_container_width=True)

def show_main_app():
    st.markdown(STYLES, unsafe_allow_html=True)
    
    st.title("📊 Text Analysis Dashboard")
    st.markdown(f"Welcome back, *{VALID_USERNAME}*!")
    
    with st.sidebar:
        st.markdown("### ⚙ Settings")
        confidence_threshold = st.slider(
            "Confidence Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.6,
            step=0.05
        )
        
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.rerun()
    
    uploaded_files = st.file_uploader(
        "📎 Upload text files for analysis",
        type=["txt"],
        accept_multiple_files=True
    )
    
    if st.button("🔍 Analyze Files", use_container_width=True):
        if not uploaded_files:
            st.warning("Please upload at least one file to analyze.")
            return
        
        with st.spinner("Processing files..."):
            try:
                files = [
                    ("files", (file.name, file.getvalue(), "text/plain"))
                    for file in uploaded_files
                ]
                
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    files=files,
                    data={"threshold": str(confidence_threshold)}
                )
                
                if response.status_code != 200:
                    st.error(f"API Error: {response.text}")
                    return
                
                results = response.json()
                
                if not results.get("results"):
                    st.info("No results to display.")
                    return
                
                valid_results = []
                for result in results["results"]:
                    if not result.get("error"):
                        valid_results.append({
                            "filename": result["filename"],
                            "sentiment_label": result["sentiment_label"],
                            "confidence": result["confidence"]
                        })
                
                if valid_results:
                    df = pd.DataFrame(valid_results)
                    
                    create_metrics_dashboard(df)
                    
                    st.markdown("### 📋 Analysis Results")
                    # Adjust table headers and columns since summary is removed
                    table_html = "<table class='styled-table'><thead><tr>"
                    headers = ["#", "Filename", "Sentiment", "Confidence", "Status"]
                    
                    for header in headers:
                        table_html += f"<th>{header}</th>"
                    
                    table_html += "</tr></thead><tbody>"
                    
                    for i, result in enumerate(results["results"], 1):
                        table_html += "<tr>"
                        table_html += f"<td>{i}</td>"
                        table_html += f"<td>{result['filename']}</td>"
                        
                        if result.get("error"):
                            table_html += "<td>N/A</td>"
                            table_html += "<td>N/A</td>"
                            table_html += f"<td>❌ {result['error']}</td>"
                        else:
                            table_html += f"<td>{result['sentiment_label']}</td>"
                            table_html += f"<td>{result['confidence']:.2%}</td>"
                            table_html += "<td>✅ Success</td>"
                        
                        table_html += "</tr>"
                    
                    table_html += "</tbody></table>"
                    st.markdown(table_html, unsafe_allow_html=True)
                    
                    create_visualizations(df)
                
            except requests.exceptions.RequestException as e:
                st.error(f"Connection Error: {str(e)}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    if st.session_state["logged_in"]:
        show_main_app()
    else:
        show_login()

if __name__ == "__main__":
    main()
