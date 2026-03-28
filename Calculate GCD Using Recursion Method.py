def GCD(a: int, b: int) -> int:
    """
    Function to calculate GCD of two numbers using recursion.

    Args:
        a (int): First number
        b (int): Second number
    Returns:
        int: Greatest Common Divisor of a and b
    Raises:
        TypeError: If inputs are not integer
        ValueError: If both numbers are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Input must be integer")

    if a == 0 and b == 0:
        raise ValueError("GCD is not defined for both values as zero")
    if b == 0:
        return a
    return GCD(b, a % b)


# -----MAIN EXECUTION------
if __name__ == "__main__":
    a = 119
    b = 544
    try:
        result = GCD(a, b)
        print("GCD is:", result)
    except TypeError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Something went wrong:", e)
