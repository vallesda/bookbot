from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def print_num_words(num_words):
    print(f"Found {num_words} total words")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        #raise Exception("Usage python3 main.py <path_to_book>")
        sys.exit(1)

    loc = sys.argv[1]   

    txt = get_book_text(loc)
    num = get_num_words(txt)
    dic = get_letters_map(txt)
    print_num_words(num)
    # Sort character counts
    sorted_characters = sort_character_counts(dic)
    print("Character Count")
    print_list_of_letters(sorted_characters)

if __name__ == "__main__":
    main()