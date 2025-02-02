def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # print(file_contents)
    print("Number of words in Frankenstein:", count_words(file_contents))
    # print(count_words("Hello worlds, how are you?"))


def count_words(book):
    word_count = 0
    words = book.split()

    for word in words:
        word_count += 1

    return word_count

main()
