import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Function to load review data from a CSV file
# This function uses pandas to read the CSV file and returns a DataFrame.
def load_data(filename):
    data = pd.read_csv(filename)
    return data

# Function to analyze the sentiment of reviews
# It uses the NLTK VADER SentimentIntensityAnalyzer to assign sentiments (positive, negative, or neutral).
def analyze_sentiment(data):
    sia = SentimentIntensityAnalyzer()
    sentiments = []
    
    for review in data['review']:
        score = sia.polarity_scores(review)
        if score['compound'] >= 0.05:
            sentiments.append('positive')
        elif score['compound'] <= -0.05:
            sentiments.append('negative')
        else:
            sentiments.append('neutral')
    
    data['sentiment'] = sentiments
    return data

# Function to calculate the average rating for each sentiment category
# It groups the DataFrame by sentiment and calculates the mean rating.
def summarize_data(data):
    summary = data.groupby('sentiment')['rating'].mean()
    return summary

# Function to display results
# Prints the sentiment analysis summary and the average ratings for each sentiment.
def display_results(data, summary):
    print("\nAverage Ratings by Sentiment:")
    print(summary)
    print("\nSentiment Analysis Summary:")
    print(data[['review', 'rating', 'sentiment']])

# Main function to orchestrate the sentiment analysis
def main():
    # Update this path to the correct location of the 'reviews.csv' file
    filename = os.path.join("reviews.csv")
    
    # Load the data
    data = load_data(filename)
    
    # Analyze sentiment
    analyzed_data = analyze_sentiment(data)
    
    # Summarize data
    summary = summarize_data(analyzed_data)
    
    # Display results
    display_results(analyzed_data, summary)

# Entry point for the script
if __name__ == '__main__':
    main()
