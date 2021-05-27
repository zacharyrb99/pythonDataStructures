def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # for value in lst:
    #     index = lst.index(value)
    #     if bool(value) == False:
    #         lst.pop(index)
    
    no_falsies = filter(bool, lst)
    return list(no_falsies)