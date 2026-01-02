import sys
from stats import word_count, char_count, sorting

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = word_count(text)
    char_counts = char_count(text)
    sorted = sorting(char_counts)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(char_counts)
    for item in sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
    print("============= END ===============")

main()
