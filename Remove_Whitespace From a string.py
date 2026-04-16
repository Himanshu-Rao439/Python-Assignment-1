def normalize_whitespace(text: str) -> str:
    """
    Normalizes whitespace in a string by:
    - Removing leading and trailing whitespace
    - Replacing multiple spaces, tabs, or newlines with a single space

    Args:
        text (str): Input string containing extra whitespace

    Returns:
        str: string with normalized whitespace

    Raises:
        TypeError: If the input is not a string
    """
    if not isinstance(text,str):
        raise TypeError("Input must be string")
    result = ""
    prev_space = False
    text.strip()
    for char in text.strip():
        # print(char)
        if not char.isspace():
            result = result + char
            prev_space = False
        else:
            if prev_space == False:
                result = result + " "
                prev_space = True
    return result

# ------Main Execution-------
if __name__ == "__main__":
    text = "this is \t\r        python"
    try:
        print(normalize_whitespace(text))
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)