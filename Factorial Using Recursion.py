def my_factorial(number: int) -> int:
    """
    Calculate the factorial of a number using recursion.

    Parameters:
    number (int): A Non-Negative integer
    Returns:
    int: Factorial of number

    Raises:
    ValueError: If Number is negative
    TypeError: If Number is not an Integer
    
    """
    # Type Validation
    if not isinstance(number,int):
        raise TypeError("Input must be integer")
    # Value Validation    
    if number < 0:
        raise ValueError("Input must be positive number")
    if number == 0 or number == 1:
        return 1

    return number * factorial(number-1)
#------MAIN EXECUTION-------
if __name__ == "__main__":
    number = 5
    try:
        result = my_factorial(number)
        print(f"Factorial of {number} is :------{result}")
    except(TypeError,ValueError) as e:
        print("Error:",e)
    except Exception as e:
        print(e)