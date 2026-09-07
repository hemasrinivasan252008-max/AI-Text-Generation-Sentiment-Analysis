import streamlit as st
from transformers import pipeline

st.title("🤖 Text Generation & Sentiment Analysis")

st.write("Enter some text and let AI generate text and analyze sentiment.")

# Sentiment Analysis Model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# Text Generation Model
text_generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

# User input
user_text = st.text_area(
    "Enter your text:",
    placeholder="Example: I am very happy today!"
)

if st.button("Analyze & Generate"):

    if user_text.strip():

        # Sentiment Analysis
        sentiment = sentiment_pipeline(user_text)[0]

        st.subheader("😊 Sentiment Analysis")
        st.write("Sentiment:", sentiment["label"])
        st.write(
            "Confidence:",
            round(sentiment["score"] * 100, 2),
            "%"
        )

        # Text Generation
        st.subheader("✍️ Generated Text")

        generated = text_generator(
            user_text,
            max_new_tokens=30,
            num_return_sequences=1
        )

        st.write(generated[0]["generated_text"])

    else:
        st.warning("Please enter some text.")