import unittest
from src.text_cleaner import TextCleaner

class TestTextCleaner(unittest.TestCase):

    def setUp(self):
        self.cleaner = TextCleaner()

    def test_clean_text_lowercase(self):
        text = "Python PROGRAMMING"
        cleaned = self.cleaner.clean_text(text)
        self.assertIn("python", cleaned)
        self.assertIn("programming", cleaned)

    def test_clean_text_punctuation(self):
        text = "Hello, world!!!"
        cleaned = self.cleaner.clean_text(text)
        self.assertEqual(cleaned, ["hello", "world"])

if __name__ == "__main__":
    unittest.main()
