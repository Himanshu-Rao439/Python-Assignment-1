def factoria_finder(num: int) -> int:
    """
    Calculate The Factorial of a non-negative integer.

    Parameters:
        num (int): The Number for which Factorial is required.
    Returns:
        int: Factorial of the given number.
    Raises:
        ValueError: If num is negetive.
        TypeError: If num is not an integer.

    """ 
    if isinstance(num,bool):
        raise TypeError("Boolean values are not Accepted")
    # check type of num
    if not isinstance(num,int):
        raise TypeError("Input must be an integer")
    # negetive check
    if num < 0:
        raise ValueError("Factorial is not defined for negetive numbers")
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
    return factorial

# main execution
if __name__ == "__main__":
    try:
        number = input("Enter your number to find Factorial : ")
        number = int(number)
        print("Factorial : ",factoria_finder(number))
    except ValueError as e:
        print("input must be an positive integer number")
    except TypeError as e:
        print("Error :",e)