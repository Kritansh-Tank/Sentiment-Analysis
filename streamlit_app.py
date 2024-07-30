import streamlit as st
from facetk import SentimentalWebcam


def run_sentiment_analysis():
    SentimentalWebcam()


st.title("Real-Time Sentiment Analysis")
if st.button("Start Analysis"):
    run_sentiment_analysis()
