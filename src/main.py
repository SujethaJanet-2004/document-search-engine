from file_loader import FileLoader
from text_cleaner import TextCleaner
from indexer import Indexer
from search_engine import SearchEngine
from highlighter import Highlighter
from stats import Stats

def main():
    print("\n=== OFFLINE DOCUMENT SEARCH ENGINE ===\n")

    # Initialize core components
    loader = FileLoader("../data")
    files_data = loader.load_files()

    cleaner = TextCleaner()
    indexer = Indexer()
    index = indexer.build_index(files_data, cleaner)

    search_engine = SearchEngine(index)
    highlighter = Highlighter(files_data)
    stats = Stats(files_data, cleaner)

    while True:
        print("\nChoose an option:")
        print("1. Search documents")
        print("2. View highlighted matches")
        print("3. Document statistics")
        print("4. Compare two documents")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        # -------------------------------------------
        # OPTION 1: Search
        # -------------------------------------------
        if choice == "1":
            query = input("\nEnter search query: ")
            results = search_engine.search(query)

            if not results:
                print("\nNo results found.")
            else:
                print("\nSearch Results (sorted):")
                for filename, score in results:
                    print(f"- {filename}  (score: {score})")

        # -------------------------------------------
        # OPTION 2: Highlighted lines
        # -------------------------------------------
        elif choice == "2":
            filename = input("\nEnter filename to highlight: ")
            query = input("Enter the same search query: ")
            query_words = query.lower().split()

            if filename not in files_data:
                print("Invalid filename.")
                continue

            lines = highlighter.highlight(filename, query_words)

            if not lines:
                print("\nNo highlighted lines found.")
            else:
                print("\nHighlighted Lines:")
                for line in lines:
                    print("- " + line)

        # -------------------------------------------
        # OPTION 3: Statistics
        # -------------------------------------------
        elif choice == "3":
            filename = input("\nEnter filename: ")

            if filename not in files_data:
                print("Invalid filename.")
                continue

            print("\n--- Statistics ---")
            print("Top 10 Words:")
            for word, count in stats.word_frequency(filename):
                print(f"{word}: {count}")

            print("\nVocabulary Size:", stats.vocabulary_size(filename))

        # -------------------------------------------
        # OPTION 4: Document similarity
        # -------------------------------------------
        elif choice == "4":
            file1 = input("\nEnter first filename: ")
            file2 = input("Enter second filename: ")

            if file1 not in files_data or file2 not in files_data:
                print("Invalid filenames.")
                continue

            sim = stats.document_similarity(file1, file2)
            print(f"\nSimilarity ({file1} vs {file2}): {sim}")

        # -------------------------------------------
        # OPTION 5: Exit
        # -------------------------------------------
        elif choice == "5":
            print("\nExiting... Goodbye!\n")
            break

        else:
            print("Invalid choice. Try again.")

# Entry point
if __name__ == "__main__":
    main()
