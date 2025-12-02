from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
import numpy as np

def tfidf_features(texts):
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(texts)
    return X, vectorizer

def word2vec_features(texts):
    tokenized = [t.split() for t in texts]
    model = Word2Vec(sentences=tokenized, vector_size=100, window=5, min_count=2)

    def sentence_vector(sentence):
        words = sentence.split()
        vectors = [model.wv[w] for w in words if w in model.wv]
        return np.mean(vectors, axis=0) if len(vectors) > 0 else np.zeros(100)

    X = np.array([sentence_vector(t) for t in texts])
    return X, model
