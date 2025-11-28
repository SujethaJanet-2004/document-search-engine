import string

class TextCleaner:
    def clean_text(self, text):
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
        return words
