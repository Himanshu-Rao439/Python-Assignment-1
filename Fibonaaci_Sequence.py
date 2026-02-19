def fibonacci_iterative(n: int) -> None:
    """
    Print Fibonaaci Sequence using iterative approach.

    Fibonaaci Sequence:
    Each number is the sum of the previous two numbers.
    Example 0 1 1 2 3 5 8 ......

    Args:
        n (int): Number of terms to print

    Raises:
        ValueError: If n is less than or equal to 0

    """
    if not isinstance(n,int):
        raise TypeError("Input N must be a integer")
    if n < 0:
        raise ValueError("Must Be be greater than zero")
        a = 0
        b = 1
        list1 = []
        for i in range(n):
            print(a,end = " ")
            a,b = b, a+b
            list1.append(a)
        print("Your list is ",list1)      
# ____________MAIN EXECUTION_____________
if __name__ == "__main__":
    n = 4
    try:
        fibonacci_iterative(n)
    except (TypeError,ValueError) as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)