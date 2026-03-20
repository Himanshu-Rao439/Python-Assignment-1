def binary_search(sorted_list: list, target: int) -> int:
    """
    Function to perform binary search on a sorted list.

    Args:
        sorted_list (list): A sorted list of integers.
        target (int): The element to search for.
    Returns:
        int: Index of the target element if found,otherwise -1.
    Raises:
        TypeError: If Input is not a list or target is not an integer.
    """
    if not isinstance(sorted_list,list):
        raise TypeError("Sorted list must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be a integer")
    low  = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high)//2
        if sorted_list[mid] == target:
            return mid
        elif target < sorted_list[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1

if __name__ == "__main__":
    sorted_list = [2,5,8,12,16,23,38,45,56,67,78,79,90,95,100]
    target = 50
    try:
        result = binary_search(sorted_list,target)
        print(result)
    except TypeError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)
        