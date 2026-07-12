import streamlit as st
from utils import load_data, prepare_dataframe, calculate_metrics
from dashboard import show_dashboard
from ai import generate_ai_analysis

st.set_page_config(
    page_title="FeedbackIQ",
    page_icon="📊",
    layout="wide"
)

st.title("📊 FeedbackIQ")
st.subheader("AI-Powered Customer Feedback Analyzer")

st.sidebar.title("📂 Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        df = load_data(uploaded_file)
        st.sidebar.success("Dataset uploaded successfully!")
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()
else:
    try:
        df = load_data("sample_feedback.csv")
        st.sidebar.info("Using sample dataset")
    except Exception as e:
        st.error(f"Could not load sample dataset: {e}")
        st.stop()

try:
    df = prepare_dataframe(df)
except Exception as e:
    st.error(str(e))
    st.stop()

metrics = calculate_metrics(df)

show_dashboard(df, metrics)

st.divider()

st.header("🤖 AI Feedback Analysis")

st.write(
    "Click the button below to analyze all customer reviews using AI."
)

if st.button("✨ Generate AI Insights"):

    reviews = df["Review"].dropna().astype(str).tolist()

    if len(reviews) == 0:
        st.warning("No reviews found in the dataset.")
    else:

        with st.spinner("Analyzing reviews..."):

            result = generate_ai_analysis(reviews)

        st.success("Analysis Completed!")

        st.markdown(result)

st.sidebar.markdown("---")

st.sidebar.header("📊 Dashboard Summary")

st.sidebar.metric(
    "Total Reviews",
    metrics["total_reviews"]
)

st.sidebar.metric(
    "Average Rating",
    metrics["average_rating"]
)

st.sidebar.metric(
    "Positive Reviews",
    metrics["positive_reviews"]
)

st.sidebar.metric(
    "Neutral Reviews",
    metrics["neutral_reviews"]
)

st.sidebar.metric(
    "Negative Reviews",
    metrics["negative_reviews"]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
FeedbackIQ can analyze customer feedback from different CSV files.

Supported review column names include:

• Review
• Feedback
• Comment
• Text
• Customer Review
• Message
• Opinion

Supported rating column names include:

• Rating
• Score
• Stars
"""
)