def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    to_swap_upper = to_swap.upper()
    to_swap_lower = to_swap.lower()

    new_phrase = ""

    for letter in phrase:
        if letter == to_swap_lower:
            new_phrase += to_swap_upper
        elif letter == to_swap_upper:
            new_phrase += to_swap_lower
        else:
            new_phrase += letter

    return new_phrase


print(flip_case('Aaaahhh', 'a'))