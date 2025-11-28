from collections import Counter
import math

class Stats:
    def __init__(self, files_data, cleaner):
        self.files_data = files_data
        self.cleaner = cleaner

    def word_frequency(self, filename):
        text = self.files_data[filename]
        words = self.cleaner.clean_text(text)
        return Counter(words).most_common(10)  # Top 10 words

    def vocabulary_size(self, filename):
        text = self.files_data[filename]
        words = self.cleaner.clean_text(text)
        return len(set(words))

    def document_similarity(self, file1, file2):
        words1 = set(self.cleaner.clean_text(self.files_data[file1]))
        words2 = set(self.cleaner.clean_text(self.files_data[file2]))

        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))

        if union == 0:
            return 0.0

        return round(intersection / union, 3)  # Jaccard similarity
