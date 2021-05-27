def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    dict = {}
    count = 0

    for key in keys:
        index = keys.index(key)
        if index < len(values):
            dict[f'{key}'] = values[index]
        else:
            dict[f'{key}'] = None

    # for key in keys:
    #     dict[f'{key}'] = None
    #     for value in values:
    #         dict[f"{key}"] = f"{value}"

    # if len(keys) <= len(values) and count == 0:
    #     while count < len(keys):
    #         dict[f'{keys[count]}'] = values[count]
    #         count += 1

    # if len(keys) > len(values):
    #     while count < len(keys):
    #         dict[f'{keys[count]}'] = None
    #         count += 1
    return dict