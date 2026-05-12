def first_non_repeated_char(text: str) -> str:
    """
    Finds and returns the first non-repeated character from a string.

    Parameters:
    text (str): The input string to check.

    Returns:
    str: The first character that appears only once.

    Raises:
    TypeError: If the input is not a string.
    ValueError: If the input string is empty.
    """
    if not isinstance(text,str):
        raise TypeError("input must be a string")
    if text == "":
        raise ValueError("input cannot be empty")
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count
    for char in text:
        if char_count[char] == 1:
            return char

# MAIN EXECUTION 
if __name__ == "__main__":
    text = "swwissn"
    try:
        print(first_non_repeated_char(text))
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)