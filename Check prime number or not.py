def is_prime(n: int) -> bool:
    """
    Check whether a given number is a prime number or not.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: 
            True  -> If the number is prime  
            False -> If the number is not prime

    Raises:
        TypeError: If the input is not an integer
    """
    if not isinstance(n,int):
        raise TypeError("Input must be a integer value")
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True
    
#------MAIN EXECUTION------
if __name__ == "__main__":
    num = int(input("Enter a number:"))
    try:
        print(is_prime(num))
    except ValueError as e:
        print("Enter a valid integer")
    except TypeError as e:
        print(e)