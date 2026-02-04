def count_vowels(text: str) -> int:
    """
    count the number of vowels in the given string.

    Parameters:
        text (str): The input string.

    Returns:
        int: Number of vowels in the string.

    Raises:
        TypeError: If the input is not a String.
    """
    # Validate if input is string or not
    if not isinstance(text,str):
        raise TypeError("Input Allow to give A only string.")
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count = count + 1
    return count
#-----Main Execution-----
if __name__ == "__main__":
    try:
        user_input = input("Enter ur string value : ")
        result = count_vowels(user_input)
        print(f"Total vowels : {result}")
    except TypeError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)