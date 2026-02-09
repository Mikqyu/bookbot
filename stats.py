def get_number_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars    

def sort_on(items):
    return items["num"]

def sort_char_counts(char_counts):
    chars_list = []
    for char, count in char_counts.items():
                chars_list.append({"char": char, "num": count})
    chars_list.sort(reverse=True, key=sort_on)  
    return chars_list  