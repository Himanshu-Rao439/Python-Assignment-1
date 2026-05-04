def flatten_list(nested_list: list) -> list:
    """
    Flattens a nested list into a single-level list.

    Args:
        nested_list (list): A list that may contain nested lists as elements.

    Parameters:
        nested_list (list): Input list which can contain integers or other lists.

    Returns:
        list: A flattened list containing all elements in a single level.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(nested_list,list):
        raise TypeError("Input Must be a list")
    result = []
    temp_list = list(nested_list)
    while temp_list:
        item = temp_list.pop()
        if isinstance(item,list):
            temp_list.extend(item) #otherwise you have a list then use extend function.
        else:
            result.append(item) #If you have a single Element then append.
    #     print("result:",result)    
    # print("final_result",result)
    return result [::-1]
if __name__ == "__main__":
    list1 = [1, [2,[3,4], 5], 6]
    try:
        print(flatten_list(list1))
    except Exception as e:
        print(e)