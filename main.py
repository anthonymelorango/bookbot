import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(path_to_file, word_count, sorted_chars):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print(f"============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # path_to_file = "books/frankenstein.txt"
    path_to_file = sys.argv[1]
    contents_of_file = get_book_text(path_to_file)
    # print(frankenstein_contents)

    word_count = count_words(contents_of_file)
    # print(f"{word_count} words found in the document")

    chars_in_file = get_char_counts(contents_of_file)
    # print(chars_in_file)

    sorted_chars = sort_dictionary(chars_in_file)
    # print(sorted_chars)

    print_report(path_to_file, word_count, sorted_chars)

main()
