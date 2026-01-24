Check number prime or not

def is_prime_number(number: int) -> bool:
    """
    Function to check whether a number is prime or not.

    Args:
        number (int): The Number to check.

    Returns:
        bool: True if the number is prime, False Otherwise.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If number is less than 2 (since primed are >= 2).
    """
    # validate input an integer
    if not isinstance(number,int):
        raise TypeError("Input must be an integer")
    # number should be at least 2
    if number < 2:
        raise ValueError("Prime Numbers are greaterv than or equal to 2")
    for i in range(2,int(number**.5)+1):
        if number % i == 0:    
            return False
            break
    else:
        return True
#Main Execution of code
if __name__ == "__main__":
    try:
        #Taking input from the user
        user_input = input("Enter the number to check its prime or not")
        # Validate and convert input to integer
        if not user_input.strip().isdigit():
            raise TypeError("Input must be a digit (no letters no strings not float")
        number = int(user_input)
        # Calling the function
        if is_prime_number(number):
            print(f"{number} is a prime numnber")
        else:
            print(f"{number} is not a prime number")
    except (TypeError,ValueError) as error:
        print(e)
    except Exception as e:
        print("Something went wrong",)
            
