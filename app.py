import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import emoji

# Load model and tokenizer
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

labels = ['Negative', 'Neutral', 'Positive']

# Function to predict sentiment
def predict_sentiment(text):
    text = emoji.emojize(text)  # handles emojis
    encoded_input = tokenizer(text, return_tensors='pt', truncation=True)
    with torch.no_grad():
        output = model(**encoded_input)
    scores = torch.nn.functional.softmax(output.logits, dim=1)
    confidence, predicted_class = torch.max(scores, dim=1)
    label = labels[predicted_class.item()]
    return label, confidence.item()

# Streamlit UI
st.title("Real-time Sentiment Analysis")
user_input = st.text_area("Enter a sentence:")

if st.button("Analyze"):
    if user_input.strip():
        label, confidence = predict_sentiment(user_input)
        st.write(f"**Sentiment:** {label}")
        st.write(f"**Confidence:** {confidence:.2f}")
    else:
        st.warning("Please enter some text.")

