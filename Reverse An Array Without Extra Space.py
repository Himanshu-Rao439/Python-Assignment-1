def reverse_array(nums: list) ->list:
    """
    Reverse the elements of a list in-place without using extra space.

    This function uses the two-pointer approach:
    - One pointer starts from the beginning.
    - Another pointer starts from the end.
    - Elements are swapped until both pointers meet.

    Parameters:
    ----------
    nums : list
        The list whose elements need to be reversed.

    Returns:
    -------
    list
        The reversed list.

    Raises:
    ------
    TypeError
        If the provided input is not a list.

    ValueError
        If the provided list is empty.
    """

    if not isinstance(nums, list):
        raise TypeError("nums must be a list")

    if nums == []:
        raise ValueError("nums cannot be empty")

    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
    if not isinstance(nums,list):
        raise TypeError("nums must be a list")
    if nums == []:
        raise ValueError("nums cannot be empty")
    left = 0
    right = len(nums) -1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left = left + 1
        right = right - 1
    return nums

#----MAIN EXECUTION----
if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7,8,9]
    try:
        print(reverse_array(nums))
    except(TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)
