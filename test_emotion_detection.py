import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def assertEmotion(self, str_to_test, expected_emotion):
        self.assertEqual(
            emotion_detector(str_to_test)["dominant_emotion"], 
            expected_emotion)

    # Test case for joy
    def test_joy(self):
        self.assertEmotion("I am glad this happened", "joy")

    # Test case for anger
    def test_anger(self):
        self.assertEmotion("I am really mad about this", "anger")

    # Test case for disgust
    def test_disgust(self):
        self.assertEmotion("I feel disgusted just hearing about this", "disgust")

    # Test case for sadness
    def test_sadness(self):
        self.assertEmotion("I am so sad about this", "sadness")

    # Test case for fear
    def test_fear(self):
        self.assertEmotion("I am really afraid that this will happen", "fear")

unittest.main()
