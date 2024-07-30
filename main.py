import streamlit as st
from facetk import SentimentalWebcam


def main():
    st.title("Sentimental Webcam")
    st.write("Webcam with sentiment analysis")

    # Instantiate SentimentalWebcam
    webcam = SentimentalWebcam()

    # Assuming SentimentalWebcam has a method to get the current frame and sentiment
    frame, sentiment = webcam.get_frame_with_sentiment()

    # Display the frame
    st.image(frame, channels="RGB")

    # Display the sentiment analysis
    st.write(f"Sentiment: {sentiment}")


if __name__ == "__main__":
    main()
