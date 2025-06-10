from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

class SentimentAnalysis:
    def __init__(self):
        pass

    def analyze_sentiment_distilbert(self, text):
        """Analyze sentiment using DistilBERT"""
        distilbert = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
        
        # Ensure text is within the token limit for DistilBERT
        try:
            result = distilbert(text[:512])[0]  # Truncate to 512 tokens
            return {
                'sentiment_distilbert': result['label'],
                'score_distilbert': result['score']
            }
        except:
            return {'sentiment_distilbert': 'ERROR', 'score_distilbert': 0}

    def get_textblob_sentiment(self, text):
        """Analyze sentiment using TextBlob"""
        analysis = TextBlob(text)

        # Determine sentiment polarity
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity < 0:
            return 'negative'
        else:
            return 'neutral'
        
    def get_vader_sentiment(self, text):
        """Analyze sentiment using VADER"""
        sia = SentimentIntensityAnalyzer()

        scores = sia.polarity_scores(text)

        # Determine sentiment based on compound score
        if scores['compound'] > 0.05:
            return 'positive'
        elif scores['compound'] < -0.05:
            return 'negative'
        else:
            return 'neutral'