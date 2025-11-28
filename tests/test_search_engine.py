import unittest
from src.search_engine import SearchEngine

class TestSearchEngine(unittest.TestCase):

    def setUp(self):
        # Fake inverted index
        self.index = {
            "python": {
                "a.txt": [1, 5, 9],
                "b.txt": [3]
            },
            "code": {
                "a.txt": [2],
                "c.txt": [4, 8]
            }
        }
        self.engine = SearchEngine(self.index)

    def test_search_single_word(self):
        result = self.engine.search("python")
        self.assertEqual(result[0][0], "a.txt")  # highest score

    def test_search_multiple_words(self):
        result = self.engine.search("python code")

        # a.txt has python (3 matches) + code (1 match) = 4
        self.assertEqual(result[0][0], "a.txt")

    def test_no_results(self):
        result = self.engine.search("nonexistingword")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
