from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        res_a = sentiment_analyzer('I love working with Python')
        self.assertEqual(res_a['label'], 'SENT_POSITIVE')
        
        res_b = sentiment_analyzer('I hate working with Python')
        self.assertEqual(res_b['label'], 'SENT_NEGATIVE')
        
        res_c = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(res_c['label'], 'SENT_NEUTRAL')

unittest.main()