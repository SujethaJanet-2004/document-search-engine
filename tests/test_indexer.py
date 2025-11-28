import unittest
from src.indexer import Indexer
from src.text_cleaner import TextCleaner

class TestIndexer(unittest.TestCase):

    def setUp(self):
        self.indexer = Indexer()
        self.cleaner = TextCleaner()
        self.files_data = {
            "file1.txt": "Python is great",
            "file2.txt": "Python is easy"
        }

    def test_build_index(self):
        index = self.indexer.build_index(self.files_data, self.cleaner)

        # Word should exist
        self.assertIn("python", index)

        # Should appear in both files
        self.assertIn("file1.txt", index["python"])
        self.assertIn("file2.txt", index["python"])

        # Positions must be stored
        self.assertIsInstance(index["python"]["file1.txt"], list)

if __name__ == "__main__":
    unittest.main()
