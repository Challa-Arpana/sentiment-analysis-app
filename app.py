import streamlit as st
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import emoji

@st.cache_resource
def load_model_and_tokenizer():
    MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    return tokenizer, model

tokenizer, model = load_model_and_tokenizer()

labels = ['Negative', 'Neutral', 'Positive']

def predict_sentiment(text):
    text = emoji.emojize(text)
    encoded_input = tokenizer(text, return_tensors='pt', truncation=True)
    with torch.no_grad():
        output = model(**encoded_input)

    print("Output logits device:", output.logits.device)
    print("Output logits tensor type:", type(output.logits))
    scores = torch.nn.functional.softmax(output.logits, dim=1)[0]
    print("Scores tensor:", scores)

    scores_dict = {label: float(score) for label, score in zip(labels, scores)}
    predicted_label = max(scores_dict, key=scores_dict.get)
    confidence = scores_dict[predicted_label]
    return predicted_label, confidence, scores_dict

st.title("Real-time Sentiment Analysis")
user_input = st.text_area("Enter a sentence:")

if st.button("Analyze"):
    if user_input.strip():
        label, confidence, scores_dict = predict_sentiment(user_input)

        emoji_map = {
            "Negative": "😞",
            "Neutral": "😐",
            "Positive": "😊"
        }

        messages = {
            "Negative": "Sorry to hear that. Stay positive! 🌈",
            "Neutral": "Thanks for sharing your thoughts.",
            "Positive": "Awesome! Glad you feel good! 🎉"
        }

        st.write(f"**Sentiment:** {emoji_map[label]} {label}")
        st.write(f"**Confidence:** {confidence:.2f}")
        st.write(messages[label])

        # Plot bar chart with thinner bars (width=0.4)
        fig, ax = plt.subplots(figsize=(5, 3))
        bars = ax.bar(scores_dict.keys(), scores_dict.values(), color=["red", "gray", "green"], width=0.4)
        ax.set_ylim([0, 1])
        ax.set_ylabel("Confidence", fontsize=10)
        ax.set_title("Sentiment Confidence Scores", fontsize=12)
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=10)

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 0.02, f'{height:.2f}', 
                    ha='center', va='bottom', fontsize=9)

        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.set_facecolor('#f9f9f9')

        fig.tight_layout()

        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.pyplot(fig)
    else:
        st.warning("Please enter some text.")

