def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    vowels_dict = {}
    phrase = phrase.lower()

    for char in phrase:
        if char in vowels:
            if vowels_dict.get(f"{char}", 0) == 0:
                vowels_dict[f"{char}"] = 1
            elif vowels_dict.get(f"{char}", 0) > 0:
                vowels_dict[f"{char}"] += 1

    return vowels_dict