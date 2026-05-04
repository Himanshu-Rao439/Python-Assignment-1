def power_of_two(n: int) -> bool:
    """
    How to check Power two Of Given N Value.

    Args.(N)

    Returns. true/false.

    TypeError: N must be integer value
    ValueError: N must be greater than zero.
    """
    if not isinstance(n,int):
        raise TypeError("N must be a integer Value")
    if n < 0:
        raise ValueError("N must be a greater than zero")
    if n > 0 and (n &(n-1)) == 0:
            return True,(n).bit_length()-1
    return False,None

#------MAIN EXECUTION-------
if __name__ == "__main__":
    n = 16
    try:
        print(power_of_two(n))
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)