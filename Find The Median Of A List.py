def find_median(nums_list: list) ->int:
    """
    Find the median value from a list of integers.

    Parameters:
        nums_list (list): List containing integer values.

    Returns:
        int | float:
            Median value of the list.
            Returns int for odd-length lists and float for even-length lists.
    """
    if not isinstance(nums_list,list):
        raise TypeError("input must be a list")
    if len(nums_list) == 0:
        raise ValueError("list cannot be empty")
    if not all(isinstance(nums_list,int) for nums_list in nums_list):
        raise ValueError("List must contains only integer")
    nums_list.sort()
    list_length = len(nums_list)
    mid = list_length // 2
    if list_length%2 != 0:
        return (nums_list[mid])
    else:
        return (nums_list[mid-1] + nums_list[mid])/2

if __name__ == "__main__":
    nums_list = [1,2,3,4,5]
    try:
        print(find_median(nums_list))
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)