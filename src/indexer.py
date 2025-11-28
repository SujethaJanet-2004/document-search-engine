class Indexer:
    def __init__(self):
        # { word: { filename: [positions] } }
        self.index = {}

    def build_index(self, files_data, cleaner):
        for filename, text in files_data.items():
            words = cleaner.clean_text(text)

            for pos, word in enumerate(words):
                if word not in self.index:
                    self.index[word] = {}

                if filename not in self.index[word]:
                    self.index[word][filename] = []

                self.index[word][filename].append(pos)

        return self.index

    def get_index(self):
        return self.index
