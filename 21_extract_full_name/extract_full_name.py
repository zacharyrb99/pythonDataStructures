names = [
    {"first": "Ada", "last": "Lovelace"},
    {"first": "Grace", "last": "Hopper"}
]

def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    full_names_list = []
    for name in names:
        first_name = name["first"]
        last_name = name["last"]
        full_name = f"{first_name} {last_name}"
        full_names_list.append(full_name)

    return full_names_list