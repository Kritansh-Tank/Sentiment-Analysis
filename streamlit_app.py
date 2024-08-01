import streamlit as st
from facetk import SentimentalWebcam

def run_sentiment_analysis():
    st.title("Sentiment Analysis")

    if st.button("Start Analysis"):
        SentimentalWebcam()

if __name__ == "__main__":
    run_sentiment_analysis()
