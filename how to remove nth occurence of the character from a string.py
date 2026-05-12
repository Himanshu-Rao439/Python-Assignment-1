def remove_nth_occurence(string:str,char_to_remove:str,n:int) -> str:
    """
    Removes the nth occurrence of a specified character from a string.

    Parameters:
        string (str): The original input string.
        char_to_remove (str): The character whose occurrence will be removed.
        n (int): The occurrence number to remove.

    Returns:
        str: A new string after removing the nth occurrence
             of the specified character.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    """
    if not isinstance(text,str):
        raise TypeError("input must be a string")
    if text == "":
        raise ValueError("Input cannot be empty")
    occurence_counter = 0
    result_characters = []
    for current_character in string:
        if current_character == char_to_remove:
            occurence_counter = occurence_counter + 1
            if occurence_counter == n:  # 2nd position
                continue
        result_characters.append(current_character)
    return "".join(result_characters)

# MAIN EXECUTION
if __name__ == "__main__":
    text = "apples are good"
    try:
        print(remove_nth_occurence(text,"a",2))
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)