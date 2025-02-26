from stats import count_words, count_letter, sort_letter_count
import sys
if len(sys.argv) < 2:
    print("Usage: python main.py <file_path>")
    sys.exit(1)

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""



def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    text = get_book_text(sys.argv[1])
    if text: # Word count section
        print("----------- Word Count ----------")
        word_count = count_words(text)
        print(f"Found {word_count} total words")
        

        # Character count section
        print("--------- Character Count -------")
        letter_count = count_letter(text)
        sorted_letters = sort_letter_count(letter_count)

        for letter_dict in sorted_letters:
            for letter, count in letter_dict.items():
                if letter.isalpha():
                    print(f"{letter}: {count}")

        print("============= END ===============")


main()