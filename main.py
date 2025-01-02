import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <book_path>")
        return

    book_path = sys.argv[1]
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        return
    #book_path = "books/frankenstein.txt"
    counter = count_words(text)
    counters = get_count_characters(text)
    char_list = []
    for key, value in counters.items():
        if key.isalpha() == True:
           char_list.append({key: value})
    char_list.sort(reverse=True, key=lambda d: list(d.values())[0])
    print(f"--- Begin report of {book_path} ---")
    print(f"{counter} words found in the document")
    for char_dict in char_list:
        char = list(char_dict.keys())[0]
        count = char_dict[char]
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def count_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def get_count_characters(text):
    lowered_text = text.lower()
    count_characters = {}
    for character in lowered_text:
            if character in count_characters:
                count_characters[character] += 1
            else:
                count_characters[character] = 1
    return count_characters



main()
