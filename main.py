def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_count(text)
    print_report(book_path, num_words, char_dict)


def sort_on(dict):
    return dict["count"]


def get_sorted_list(char_dict):
    char_list = []

    for key in char_dict:
        if key.isalpha():
            char_list.append({"name": key, "count": char_dict[key]})

    char_list.sort(reverse=True, key=sort_on)

    return char_list


def print_report(book_path, word_count, char_dict):

    char_list = get_sorted_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for c_dict in char_list:
        print(f"The '{c_dict["name"]}' character was found {c_dict["count"]} times")

    print("--- End report ---")


def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


main()
