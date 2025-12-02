import pandas as pd
import snscrape.modules.twitter as sntwitter

def scrape_tweets(keyword, limit=200):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(keyword).get_items()):
        if i > limit:
            break
        tweets.append([tweet.date, tweet.content])
    df = pd.DataFrame(tweets, columns=["date", "text"])
    df.to_csv("data/tweets.csv", index=False)
    return df

if __name__ == "__main__":
    scrape_tweets("technology -filter:retweets", limit=500)
