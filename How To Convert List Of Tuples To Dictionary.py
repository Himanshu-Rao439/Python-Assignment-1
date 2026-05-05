def list_to_dict(List: list) -> dict:
    """
    Convert a list of (key, value) tuples into a dictionary.

    Args:
        data (list): List of tuples.

    Returns:
        dict: Converted dictionary.

    Raises:
    
    TypeError: If input is not a list or elements are not tuples.
    
    """
    if not isinstance(data,list):
        raise TypeError("input must be a list")
    my_dict = {}
    for key,value in List:
        my_dict[key] = value
    return my_dict

if __name__ == "__main__":
    data = [('a',1),('b',2),('c',3),('d',4)]
    try:
        print(list_to_dict(data))
    except Exception as e:
        print(e)