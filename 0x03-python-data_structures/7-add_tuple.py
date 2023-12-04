#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Write a function that adds 2 tuples
    Returns a tuple with 2 integers:
    The first element should be the addition of
    the first element of each argument
    The second element should be the addition of
    the second element of each argument
    """
    if tuple_a is None and tuple_b is None:
        return None
    if len(tuple_a) == 1:
        a = (tuple_a[0], 0)
    else:
        a = (0, 0) if not tuple_a else tuple_a[:2]
    if len(tuple_b) == 1:
        b = (tuple_b[0], 0)
    else:
        b = (0, 0) if not tuple_b else tuple_b[:2]

    new_tuple = (a[0] + b[0], a[1] + b[1])

    return new_tuple
