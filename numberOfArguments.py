def numberOfArguments(*args, **kwargs):
    """
    numberOfArguments  prints an unknown number of arguments received by the function.
    :param args: list of arguments.
    :param kwargs: dictionary of keyword arguments.
    """
    print("\nFunction got arguments: ")

    for valueOnArgs in args:
        print(valueOnArgs)

    for name, value in kwargs.items():
        print(f"\nFunction got argument ---> name: {name}   value: {value}")


# Test
numberOfArguments(4, 8, 2, 1, 6, Nadav=31, Gil=28, Nofar=32)
