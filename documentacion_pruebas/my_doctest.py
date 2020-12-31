def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    >>> suma(5, 10)
    15
    >>> suma(0, 0)
    1
    >>> suma(-5, 7)
    2
    """
    return a + b


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
