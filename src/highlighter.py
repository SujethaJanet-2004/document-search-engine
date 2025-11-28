class Highlighter:
    def __init__(self, files_data):
        self.files_data = files_data

    def highlight(self, filename, query_words):
        text = self.files_data[filename]
        lines = text.split("\n")

        highlighted_lines = []

        for line in lines:
            lower_line = line.lower()

            if any(word.lower() in lower_line for word in query_words):
                highlighted = line
                for word in query_words:
                    highlighted = highlighted.replace(
                        word,
                        f">>>{word}<<<"
                    )
                highlighted_lines.append(highlighted)

        return highlighted_lines
