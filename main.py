def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_character_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    sorted_list = print_report(characters, num_words)

    # Then in your main code:
    #word_count = get_word_count()  # or however you're getting this
    #char_freq = get_char_frequency()  # or however you're getting this
    #print_report(char_freq, word_count)



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

def print_report(char_freq, word_count):
    list = []
    for letter, count in char_freq.items():
        if letter.isalpha():
            dict = {"char": letter, "num" : count}
            list.append(dict)

    def sort_on(dict):
        return dict["num"]

    list.sort(reverse = True, key = sort_on)
    for letters in list:
        print(f"The '{letters['char']}' character was found {letters['num']} times")
main()
