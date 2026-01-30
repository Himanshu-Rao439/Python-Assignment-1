def is_palindrome(text:str) -> bool:
    """
    checks whether a given string is a palindrome.

    Returns:
        Returns a True if string is a palindrome False Otherwise.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input is string is empty.

    """        
    # 1. Input must be a string
    if not isinstance(text,str):
        raise TypeError("Input must be a string")
    # 2. String must not be empty
    if text.strip() == "":
        raise ValueError("input string can not empty")
    else:
        text = text.strip().lower()
    # Reverse the string
    reverse_string = ""
    for ch in text:
        reverse_string = ch + reverse_string
    return text == reverse_string
#--------Main Execution--------
if __name__ == "__main__":
    try:
        user_input = input("Enter Your string to check:").strip().lower()
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome")
        else:
            print(f"{user_input} is not a palindrome")
    except(TypeError,ValueError) as e:
        print("Error:",e)