# Real-time Sentiment Analysis Web App

This project is a real-time sentiment analysis app using the **RoBERTa model** from Hugging Face Transformers.  
Built with **Python**, **Streamlit**, and **PyTorch**, it predicts the sentiment of any text input and visualizes the result using emoji feedback and model confidence scores.

---

## 🌐 Live Demo
➡️ [Try the App Here](https://challa-sentiment-analyzer.streamlit.app/) 

---

## 🔍 Features

- ✅ Real-time sentiment prediction  
- 📊 Confidence bar chart visualization  
- 😊 Friendly feedback using emojis and messages  
- 💬 Easy-to-use Streamlit interface  

---

## 🧪 Try These Example Sentences:

Test the app with any custom text, or try these examples:

- “I love it here! 😍 This place is magical.” ✅  
- “I’m so disappointed in how this turned out.” ❌  
- “I went to the store and bought some milk.” 😐  
- “Ugh... that was such a waste of time. 😤”  
- “You always support me and I’m grateful.” 🙏

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

## 📸 Demo GIF

![Demo GIF](https://raw.githubusercontent.com/Challa-Arpana/sentiment-analysis-app/master/demo.gif)

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
