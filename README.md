# Real-time Sentiment Analysis Web App

This is a real-time sentiment analysis web application built with **Streamlit** using the **RoBERTa** model from Hugging Face. It predicts whether a given sentence is **Positive**, **Neutral**, or **Negative**, and displays results with **confidence scores**, **bar charts**, and **emojis** for a friendlier experience.

---

## 🔍 Features

- ✅ Real-time sentiment prediction  
- 📊 Confidence bar chart visualization  
- 😊 Friendly feedback using emojis and messages  
- 💬 Easy-to-use Streamlit interface  

---

## 🛠 Technologies Used

- Python  
- Streamlit  
- Hugging Face Transformers  
- PyTorch  
- Matplotlib  
- Emoji  

---

## 🚀 How to Run the App Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Challa-Arpana/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # For Windows
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

---

## 🤖 Model Details

We use the [`cardiffnlp/twitter-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) model from Hugging Face. It classifies input into one of three sentiments:

- **Negative** 😞  
- **Neutral** 😐  
- **Positive** 😊  

This model is specifically trained on social media text like tweets and performs well on short, informal sentences.

---

## 👤 Author

**Arpana Challa**  
🌐 GitHub: [Challa-Arpana](https://github.com/Challa-Arpana)  
🔗 LinkedIn: [Arpana Challa](https://www.linkedin.com/in/arpana-challa-6626a9196)

---
