def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dictionary = get_chars_in_string(text)
    char_sorted = sort_chars_to_list(char_dictionary)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_chars_in_string(text):
    chars = {}
    for i in text:
        lowercase = i.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else:
            chars[lowercase] = 1
    return chars

def sort_chars_to_list(char_dict):
    sorted = []
    for i in char_dict:
        sorted.append({"char": i, "num": char_dict[i]})
    sorted.sort(reverse = True, key = sort_on)
    return sorted

def sort_on(i):
    return i["num"]

main()