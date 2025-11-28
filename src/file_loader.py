import os

class FileLoader:
    def __init__(self, folder_path="../data"):
        self.folder_path = folder_path

    def load_files(self):
        files_data = {}
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                path = os.path.join(self.folder_path, filename)
                with open(path, "r", encoding="utf-8") as f:
                    files_data[filename] = f.read()
        return files_data
