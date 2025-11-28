class SearchEngine:
    def __init__(self, index):
        self.index = index

    def search(self, query):
        query_words = query.lower().split()

        scores = {}  
        # {filename: score}

        for word in query_words:
            if word in self.index:
                for filename, positions in self.index[word].items():
                    if filename not in scores:
                        scores[filename] = 0
                    scores[filename] += len(positions)  # Frequency = relevance

        if not scores:
            return []

        # Sort by score (high → low)
        results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return results
