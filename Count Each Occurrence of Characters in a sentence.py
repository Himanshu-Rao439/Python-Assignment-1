def count_characters(input_string: str) -> dict:
    """
    Function to count the occurrences of each character in a string.

    Args:
        input_string (str): The string whose characters are to be counted.
    Returns:
        dict: A Dictionary with characters as keys and thier counts as value.
    Raises:
        TypeError: If Input is not a string.
    """    
    # Validate the input type
    if not isinstance(input_string,str):
        raise TypeError("Input must be a string")
    char_count = {}
    for char in input_string.lower().replace(" ",""):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1    
    return char_count
#------MAIN EXECUTION-------
if __name__ == "__main__":
    user_input = "APPLE"
    try:
        result = count_characters(user_input)
        print(result)
    except TypeError as e:
        print("Error:",e)
    except Exception as e:
        print(e)