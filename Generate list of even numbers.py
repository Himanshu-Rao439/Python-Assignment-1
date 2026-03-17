def generate_even_number_lists(n:int) -> int:
    """
    Function to Generate a list of even numbers from 1 to n.

    Args:
        n (int): Upper limit

    Returns:
        list: List of even numbers from 1 to n

    Raises:
        TypeError: If Input is not an integer
        ValueError:If N is less than 1
    """
    if not isinstance(n,int):
        raise TypeError("Input must be integer")
    if n<=2:
        raise ValueError("INput must be greater than or equal to 2")
    even_number_list = [i for i in range (2,n+1,2)]
    return even_number_list

#-----MAIN EXECUTION-----
if __name__ == "__main__":
    n = 20
    try:
        result = generate_even_number_lists(n)
        print("Even Number List:",result)
    except (TypeError,ValueError) as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)