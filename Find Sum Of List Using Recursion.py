def recursive_sum(list1: list) -> int:
    """
    Calculate the sum of a list of list1 using recursion.

    Args:
        list1 (list): List containing numeric values
    Returns:
        int or float: Sum of all elements in the list
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: if the list is empty
    """
    if not isinstance(list1, list):
        raise TypeError("list must be list")

    if len(list1) == 0:
        raise ValueError("list can not be empty")

    if not isinstance(list1[0], (int, float)):
        raise TypeError("list can contain only numeric value")

    if len(list1) == 1:  
        return list1[0]

    return list1[0] + recursive_sum(list1[1:])


if __name__ == "__main__":
    list1 = [10,20,30,40]
    try:
        print(recursive_sum(list1))
    except (TypeError, ValueError) as e:
        print(e)
    