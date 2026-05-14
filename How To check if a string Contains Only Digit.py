def is_all_digits(text: str) -> bool:
    """
    Checks whether the given string contains only digit characters (0–9).

    Parameters:
        text (str): The input string to validate.

    Returns:
        bool:
            True  -> if all characters in the string are digits.
            False -> if any character is not a digit.

    Raises:
        TypeError:
            If the input string is empty.

        ValueError:
            If the input is not of type string.
    """
    if text == "":
        raise TypeError("input cannot be empty")
    if not isinstance(text,str):
        raise ValueError("input must be a form of string")
    for char in text:
        if char < "0" or char > "9":
            return False
        
    return True

if __name__ == "__main__":
    text = "12345"
    try:
        print(is_all_digits(text))
    except(TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)