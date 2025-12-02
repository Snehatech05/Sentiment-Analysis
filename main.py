import pandas as pd
from src.data_cleaning import clean_text
from src.feature_engineering import tfidf_features
from src.model_training import train_model
from src.visualization import plot_sentiment_counts

df = pd.read_csv("data/tweets.csv")
df["cleaned"] = df["text"].apply(clean_text)

import random
df["sentiment"] = [random.choice(["positive", "negative", "neutral"]) for _ in range(len(df))]

plot_sentiment_counts(df)

X, vectorizer = tfidf_features(df["cleaned"])
y = df["sentiment"]
model = train_model(X, y)
