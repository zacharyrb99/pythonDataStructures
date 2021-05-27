def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # letter_dictionary = {}

    # for letter in phrase:
    #     if letter_dictionary.get(f"{letter}", None) == None:
    #         letter_dictionary[f"{letter}"] = 1

    #     elif letter_dictionary[f"{letter}"]:
    #         letter_dictionary[f"{letter}"] += 1
    
    # return letter_dictionary
    
    letters = {char: phrase.count(char) for char in phrase}
    return letters