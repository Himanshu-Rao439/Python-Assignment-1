def is_prime_number(n: int) -> int:
    """
    Check whether a number is prime or not.

    Parameters:
        n (int): Integer value to check.
    
    TypeError: Input must be a integer value
    
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
    try:
        prime_number_list = []
        lower_limit = input("Enter Your Lower Limit:")
        upper_limit = input("Enter Your Upper Limit:")
        if not lower_limit.strip().isdigit():
            raise TypeError("Lower limit must be a valid integer (no decimals or letters).")
        if not upper_limit.strip().isdigit():
            raise TypeError("Upper Limit must be a valid integer (no decimals or letters).")
        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)
        
        
        for i in range(lower_limit,upper_limit):
            if is_prime_number(i):
                print(f"{i} prime number")
                prime_number_list.append(i)
        print(prime_number_list)
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)