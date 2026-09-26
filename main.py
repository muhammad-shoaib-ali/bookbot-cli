from stats import word_count
from stats import get_character_count
from stats import chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as file:
        return file.read()


def print_report(book_path,words,sorted_characters):
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("----------- Character Count ----------")
    for char, count in sorted_characters:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def main():
    book_text = get_book_text('books/frankenstein.txt')
    book_path = 'books/frankenstein.txt'
    words = word_count(book_text)
    characters = get_character_count(book_text)
    sorted_characters = chars_dict_to_sorted_list(characters)
    print_report(book_path, words, sorted_characters)

main()
