def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_character_dict(text)
    print(f"{num_words} words found in the document")
    print(characters)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_character_dict(text):
    dict = {}
    lowered_string = text.lower()
    for letter in lowered_string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict



main()
