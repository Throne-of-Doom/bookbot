def count_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_letter(text):
    """
    Counts the occurrences of each letter in a given text.

    Args:
        text (str): The text to count letters in.

    Returns:
        dict: A dictionary with letters as keys and their counts as values.
    """
    count_letter = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in count_letter:
            count_letter[lower_letter] += 1
        else:
            count_letter[lower_letter] = 1
    return count_letter

def get_count(count_letter):
     return list(count_letter.values())[0]

def sort_letter_count(count_letter):
    """
    Sorts the letter count dictionary by letter.

    Args:
        count_letter (dict): A dictionary with letters as keys and their counts as values.

    Returns:
        dict: A sorted dictionary by letter.
    """

    sorted_letters = [{letter: count} for letter, count in count_letter.items()]
    sorted_letters.sort(reverse=True, key=get_count)
    return sorted_letters

