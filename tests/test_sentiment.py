import unittest
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from scripts.sentiment_analysis import SentimentAnalysis 

class TestSentimentAnalysis(unittest.TestCase):
    def setUp(self):
        self.sa = SentimentAnalysis()
    
    def test_analyze_sentiment_distilbert(self):
        text = "I love this product!"
        result = self.sa.analyze_sentiment_distilbert(text)
        
        # Check that the result is a dict with keys
        self.assertIsInstance(result, dict)
        self.assertIn('sentiment_distilbert', result)
        self.assertIn('score_distilbert', result)
        
        # sentiment label should be string and score a float
        self.assertIsInstance(result['sentiment_distilbert'], str)
        self.assertIsInstance(result['score_distilbert'], float)
        
        # The label should be one of expected values
        self.assertIn(result['sentiment_distilbert'], ['POSITIVE', 'NEGATIVE', 'ERROR'])
        
    def test_get_textblob_sentiment(self):
        self.assertEqual(self.sa.get_textblob_sentiment("I love it"), 'positive')
        self.assertEqual(self.sa.get_textblob_sentiment("I hate it"), 'negative')
        
    def test_get_vader_sentiment(self):
        self.assertEqual(self.sa.get_vader_sentiment("I love it"), 'positive')
        self.assertEqual(self.sa.get_vader_sentiment("I hate it"), 'negative')

if __name__ == "__main__":
    unittest.main()
