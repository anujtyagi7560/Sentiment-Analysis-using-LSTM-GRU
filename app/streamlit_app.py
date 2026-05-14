import streamlit as st
import sys
import os

# Add src folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from predict import predict_sentiment

st.title("Yelp Review Sentiment Analysis")

review = st.text_area("Enter Review")

if st.button("Analyze"):

    if review.strip():

        sentiment, confidence = predict_sentiment(review)

        st.success(f"Prediction: {sentiment}")

        st.write(f"Confidence: {confidence:.4f}")