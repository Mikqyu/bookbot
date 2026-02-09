import sys


def get_book_text(filepath):
    with open(filepath) as f:
        filecontent = f.read()
    return filecontent



from stats import get_number_words, get_chars_dict, sort_char_counts



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    text = get_book_text(sys.argv[1])
    num_words = get_number_words(text)
    characters = get_chars_dict(text)
    sorted_list = sort_char_counts(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")
main()