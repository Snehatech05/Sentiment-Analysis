import seaborn as sns
import matplotlib.pyplot as plt

def plot_sentiment_counts(df):
    sns.countplot(data=df, x="sentiment")
    plt.title("Sentiment Distribution")
    plt.show()
