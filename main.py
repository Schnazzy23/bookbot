def main():
    book = "books/frankenstein.txt"
    text = file_contents(book)
    number_of_words = count_words(text)
    char_dict = count_characters(text)
    sorted_list = convert_to_list(char_dict)

    print(f"--- Begin report of {book} ---")
    print(f"{number_of_words} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def convert_to_list(char_dict):
    sorted_list = []
    for c in char_dict:
        sorted_list.append({"char": c, "num": char_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def file_contents(book):
    with open(book) as f:
        contents = f.read()
    return contents

main()
