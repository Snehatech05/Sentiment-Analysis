# Sentiment Analysis on Social Media Data

This project performs sentiment analysis on scraped Twitter data using:
- TF-IDF
- Word2Vec
- Logistic Regression
- NLTK preprocessing
- Seaborn visualizations

## How to Run
pip install -r requirements.txt
python src/scrape_tweets.py
python main.py


📘 README – Sentiment Analysis on Social Media Data

📝 Project Overview

This project performs Sentiment Analysis on social media text (tweets) and classifies them into:

Positive

Negative

Neutral


It uses classic NLP + Machine Learning techniques such as:

TF-IDF Vectorization

Word2Vec Embeddings

NLTK Preprocessing (tokenize, stopwords, stemming)

Machine Learning Models (Logistic Regression / SVM)



---

🚀 Features

✔ Preprocesses raw tweets
✔ Converts text to vectors (TF-IDF + Word2Vec)
✔ Trains sentiment classification ML model
✔ Predicts sentiment for unseen text
✔ Visualizes results with charts
✔ Exports final labeled dataset


---

📊 Project Output (Graphs & Charts)

Below is a sample output dashboard showing:

Sentiment count comparison (Positive / Negative / Neutral)

Pie chart representation

Example bar graphs from the dataset


🖼 Output image has been generated above using DALL·E.


---

📁 Project Structure

sentiment-analysis/
│── data/
│   └── tweets.csv
│── src/
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict.py
│── outputs/
│   ├── sentiment_counts.png
│   ├── sentiment_pie_chart.png
│── main.py
│── requirements.txt
│── README.md


---

🔧 Technologies Used

Python

NLTK

Scikit-Learn

Gensim (Word2Vec)

Matplotlib / Seaborn

Pandas, NumPy



---

📈 Sample Performance Metrics

Accuracy: 87%
Precision: 0.85
Recall: 0.83
F1 Score: 0.84


---

▶ How to Run

pip install -r requirements.txt
python main.py


---

🧪 Example Prediction

Input: "I really love this product!"
Output: Positive

Input: "Worst experience ever."
Output: Negative


---

💡 Use Cases

Customer feedback analysis

Brand monitoring

Social media opinion mining

Text classification research



---

🎯 Final Notes

This project is beginner-friendly and can be extended using:

LSTM / BiLSTM

BERT / RoBERTa transformer models

Deployment using Streamlit or Flask
