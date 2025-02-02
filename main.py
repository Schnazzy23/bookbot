def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # print(file_contents)
    print("Number of words in Frankenstein:", count_words(file_contents))
    print("Number of words in Frankenstein:", count_characters(file_contents))


def count_words(book):
    word_count = 0
    words = book.split()

    for word in words:
        word_count += 1

    return word_count

def count_characters(book):
    lowered = book.lower()
    number_of_words = {}
    
    for character in lowered:
        if character in number_of_words:
            number_of_words[character] += 1
        else:
            number_of_words[character] = 1

    return number_of_words

main()
