def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_chars_to_list(char_dict):
    sorted = []
    for i in char_dict:
        sorted.append({"char": i, "num": char_dict[i]})
    sorted.sort(reverse = True, key = sort_on)
    return sorted

def sort_on(i):
    return i["num"]