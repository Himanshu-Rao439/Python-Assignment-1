def binary_to_decimal(binary_str):
    """
    Convert a binary string into its decimal equivalent.

    Parameters:
    ----------
    binary_str : str
        A string containing a binary number.

    Returns:
    -------
    int
        Decimal representation of the binary number.
    """
    if not isinstance(binary_str,str):
        raise TypeError("input must be string")
    if binary_str == "":
        raise ValueError("input cannot be empty")
    total = 0
    power = 0
    for digit in reversed(binary_str):
        if digit == "1": 
            total = total + 2**power
        power = power + 1
    return total

if __name__ == "__main__":
    binary_str = "1011"
    try:
        print(binary_to_decimal(binary_str))
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)