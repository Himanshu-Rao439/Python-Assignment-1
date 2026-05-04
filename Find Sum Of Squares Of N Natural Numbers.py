def sum_of_squares(n: int) ->int:
    """
    Calculate sum of squares using mathematical Formula.
    Returns:
        n(integer) Value.
    Arg:
        (n).
    Raises:
        TypeError: N must be an integer.
        ValueError N must be positive number.
    """
    if not isinstance(n,int):
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be a positive number")
    total = (n*(n+1)*(2*n+1)//6)
    return total
if __name__ == "__main__":
    try:
        n = 3
        result = sum_of_squares(n)
        print("Sum Of Squares:",result)
    except Exception as e:
        print(e)