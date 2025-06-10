# sentiment_model.py
from transformers import pipeline

# Load pre-trained sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = round(result['score'], 2)
    return label, score
