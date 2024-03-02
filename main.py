import string


def main():
    with open(
        "/Users/peterwilliams/self_learning/boot_dev/projects/book_bot_text_analysis/books/frankenstein.txt"
    ) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

        letter_count = count_letters(words)
        word_count_report(letter_count)


def count_letters(word_list):
    letter_count = {letter: 0 for letter in string.ascii_lowercase}

    for word in word_list:
        for letter in word:
            if letter.isalpha():
                letter_count[letter.lower()] += 1
    return letter_count


def word_count_report(letter_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(letter_count.items(), "these are the items")
    sorted_letter_count = sorted(
        letter_count.items(), key=lambda item: item[1], reverse=True
    )

    for letter, count in sorted_letter_count:
        print(f"The character {letter} was found {count} times")

    print("--- End report of books/frankenstein.txt ---")


main()
