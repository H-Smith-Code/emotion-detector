from EmotionDetection.emotion_detection import emotion_detection
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy emotion
        result_1 = emotion_detection('I am glad this happened')
        self.assertEqual(result_1['label'], 'joy')
        # Test case for anger emotion
        result_2 = emotion_detection('I am really mad about this')
        self.assertEqual(result_2['label'], 'anger')
        # Test case for disgust emotion
        result_3 = emotion_detection('I feel disgusted just hearing about this')
        self.assertEqual(result_3['label'], 'disgust')
        # Test case for sadness emotion
        result_4 = emotion_detection('I feel disgusted just hearing about this')
        self.assertEqual(result_4['label'], 'sadness')
        # Test case for fear emotion
        result_5 = emotion_detection('I feel disgusted just hearing about this')
        self.assertEqual(result_5['label'], 'fear')

unittest.main