def swap_numbers(a,b):
    """
    Swap two integer numbers.

    Parameters:
    ----------
    a : int
        First integer number.

    b : int
        Second integer number.
    """
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("inputs must be a integer value")
    a,b = b,a
    return a,b
if __name__ == "__main__":
    a = 5
    b = 3
    try:
        print("a before swap:",a)
        print("b before swap:",b)
        a,b = swap_numbers(a,b)
        print("a after swap:",a)
        print("b after swap:",b)
    except Exception as e:
        print(e)