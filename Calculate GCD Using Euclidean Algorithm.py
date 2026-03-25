def GCD(a: int,b: int) -> int:
    """
    Function to calculate GCD of two numbers.

    Args:
        a (int): First number
        b (int): Second number
    Returns:
        int: Greatest Common Divisor of a and b
    Raises:
        TypeError: If inputs are not integer
        ValueError: If both numbers are zero
    """
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("Input must be integer")
    if a == 0 and b == 0:
        raise ValueError("GCD is not defined for both values as zero")
    a,b = abs(a),abs(b)
    while b != 0:
            a,b = b,a%b
    return a
#----MAIN EXECUTION----
if __name__ == "__main__":
    a = 50
    b = 60
    try:
        result = GCD(a,b)
        print("GCD is :",result)
    except TypeError as e:
        print("Error:",e)
    except ValueError as e:
        print("Error:",e)
    except Exception as e:
        print("Somothing went wrong",e)