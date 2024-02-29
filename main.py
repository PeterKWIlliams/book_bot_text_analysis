def main():
    with open(
        "/Users/peterwilliams/self_learning/boot_dev/projects/book_bot_text_analysis/books/frankenstein.txt"
    ) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

    def letter_count(word_list):
        letters = list(range(ord("a"), ord("z") + 1))
        letter_count = {}

        for word in word_list:
            for letter in word:
                if ord(letter.lower()) in letters:
                    if letter.lower() not in letter_count:
                        letter_count[letter.lower()] = 1
                    else:
                        letter_count[letter.lower()] += 1
                else:
                    None
        return letter_count

    def sort_on(dict):
        return dict["count"]

    def word_count_report(letter_count):
        sorted_letter_count = []
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"Total words: {len(words)}")
        for key in letter_count:
            sorted_letter_count.append({"letter": key, "count": letter_count[key]})

        sorted_letter_count.sort(reverse=True, key=sort_on)

        for dict in sorted_letter_count:
            print(f"The character {dict['letter']} was found {dict['count']} times")

        print("--- End report of books/frankenstein.txt ---")

    letter_count = letter_count(words)
    word_count_report(letter_count)


main()
