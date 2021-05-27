def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    for char in phrase:
        if char == to_swap:
            if to_swap.isupper():
                return phrase.replace(to_swap, to_swap.lower())
            elif to_swap.islower():
                return phrase.replace(to_swap, to_swap.upper())