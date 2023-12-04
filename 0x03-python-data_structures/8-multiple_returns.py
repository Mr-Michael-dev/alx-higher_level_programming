#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character."""
    my_tuple = tuple(sentencei)
    length = len(my_tuple)

    if length == 0:
        first_char = None
    else:
        first_char = my_tuple[0]

    return length, first_char
