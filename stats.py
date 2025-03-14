def get_num_words(book_text):
    return len(book_text.split())

def get_letters_map(book_text):
    letter_map = {}
    for c in book_text:
        current = c.lower()
        if current not in letter_map:
            letter_map[current] = 0
        letter_map[current] += 1
    return letter_map

def sort_character_counts(char_counts):
    sorted_list = [
        [char, count]
        for char, count in char_counts.items() if char.isalpha()
    ]
    
    # Sort the list by count in descending order
    sorted_list.sort(key=lambda x: x[1], reverse=True)
    
    return sorted_list

def print_list_of_letters(char_list):
    for p in char_list:
        print(f"{p[0]}: {p[1]}")