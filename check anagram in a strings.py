def is_anagram(string1: str, string2: str) -> bool:
    """
    check whether two strings are anagrams using character counting.
    Spaces are ignored and comparison is case-insensitive.

    Parameters:
        string1 (str): First input string
        string2 (str): Second Input string

    Returns:
        bool: True if strings are anagrams, False otherwise

    Raises:
        TypeError: If either input is not a string

    """   
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("Input must be string.")
    string1 = string1.replace(" ","").lower() 
    string2 = string2.replace(" ","").lower() 
    if len(string1) != len(string2):
        return False
    char_count = {}
    for char in string1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string2:
        if char not in char_count:
            print("True for",char)
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            print("true for",char)
            return False
            break
    else:
        return True
if __name__ == "__main__":
    string1 = "race"
    string2 = "care"
    try:
        result = is_anagram(string1,string2)
        if result:
            print("Your string is anagram")
        else:
            print("Your String is not anagram")
    except TypeError as e:
        print(e)
