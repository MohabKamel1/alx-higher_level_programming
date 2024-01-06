#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    default_value = 0
    tuple_a = tuple_a + (default_value,) * (max(len(tuple_a), len(tuple_b)) - len(tuple_a))
    tuple_b = tuple_b + (default_value,) * (max(len(tuple_a), len(tuple_b)) - len(tuple_b))

    return tuple(a + b for a, b in zip(tuple_a, tuple_b))[:2]
