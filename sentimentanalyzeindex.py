from newsapi import NewsApiClient
import twint

# Initialize News API client with your API key
newsapi = NewsApiClient(api_key='apikey')

import yfinance as yf
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Function to fetch historical stock data
def get_stock_data(stock_symbol, start_date, end_date):
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data

# Function to fetch tweets related to a stock
def get_stock_tweets(stock_symbol, since_date, until_date):
    c = twint.Config()
    c.Search = stock_symbol
    c.Since = since_date
    c.Until = until_date
    c.Lang = 'en'
    c.Limit = 100  # Adjust the limit as needed
    c.Pandas = True
    twint.run.Search(c)
    tweets = twint.storage.panda.Tweets_df['tweet']
    return tweets


# Function to fetch news articles related to a stock
def get_stock_news(stock_symbol, from_date, to_date):
    articles = newsapi.get_everything(q=stock_symbol, from_param=from_date, to=to_date, language='en')
    try:
        return [article['title'] + ' ' + article['description'] for article in articles['articles']]
    except: return ['']


# Function to perform sentiment analysis
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)
    return sentiment_score['compound']

# Function to rank sentiment for each stock
def rank_sentiment_for_stocks(stock_symbols, start_date, end_date):
    sentiments = {}
    for symbol in stock_symbols:
        # Fetch historical stock data
        stock_data = get_stock_data(symbol, start_date, end_date)
        # Aggregate news or social media posts related to the stock
        # For demonstration purposes, let's assume we have a list of texts in 'texts'
        try:
            texts = get_stock_tweets(symbol,start_date,end_date)
            combined_text = ' '.join(texts)
        except: continue 
        # Perform sentiment analysis on combined text
        sentiment_score = analyze_sentiment(combined_text)
        sentiments[symbol] = sentiment_score
    # Rank stocks based on sentiment score
    ranked_stocks = sorted(sentiments.items(), key=lambda x: x[1], reverse=True)
    return ranked_stocks

# Example usage
if __name__ == "__main__":
    # Dow Jones Industrial Average (DJIA) stocks
    dow_stocks = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'BRK-B', 'JPM', 'JNJ', 'V', 'PG',
                  'MA', 'UNH', 'INTC', 'HD', 'VZ', 'T', 'MRK', 'NVDA', 'ADBE', 'DIS', 'CRM',
                  'NFLX', 'CMCSA', 'XOM', 'CSCO']
    start_date = '2024-04-22'
    end_date = '2024-04-29'
    ranked_stocks = rank_sentiment_for_stocks(dow_stocks, start_date, end_date)
    print("Ranked Stocks based on Sentiment:")
    for rank, (stock, sentiment) in enumerate(ranked_stocks, start=1):
        print(f"{rank}. {stock}: Sentiment Score - {sentiment:.4f}")



