import sys
from stats import (
    get_num_words, 
    get_chars_dict, 
    sort_chars_to_list
)

if len(sys.argv) < 2:
    raise Exception("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dictionary = get_chars_dict(text)
    char_sorted = sort_chars_to_list(char_dictionary)

    print_report(book_path, num_words, char_sorted)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()