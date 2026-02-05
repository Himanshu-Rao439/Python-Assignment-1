def sum_of_digits(n: int) -> int:
    """
    Calculate the sum of digits of a non-negative integer.

    Parameters:
    n (int): The Number whose digits will be summed.

    Returns:
        int: Sum of the Digits.

    Raises:
        TypeError: If Input is not an integer.
        ValueError: If input is negative.
    """    
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    total = 0
    while n:
        total += n % 10
        n //= 10
    return total


# ------- MAIN EXECUTION -------
if __name__ == "__main__":
    try:
        num = int(input("Enter your number: "))
        print("Sum of digits:", sum_of_digits(num))
    except (TypeError, ValueError) as e:
        print("Error:", e)
