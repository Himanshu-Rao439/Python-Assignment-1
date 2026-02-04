from typing import List
def second_largest(nums : List[int]) -> int:
    """
    Find the second largest unique number in a list without using sorting.

    Parameters:
        nums (List[int]): A list of integer.

    Returns:
        int: The Second laregest unique value.

    Raises:
        TypeError: if input is not a list or elements are not integers.
        ValueError: if the list has fewer than 2 unique elements.
    """
    # Validate that the input is a list
    if not isinstance(nums,list):
        raise TypeError("input must be a list of integers.")
    # Validate that all elements in the list are integers
    if any(not isinstance(current_number,int) for current_number in nums):
        raise TypeError("All Elements of list should be integers.")
    # check list has atleast two elements
    if len(nums) < 2:
        raise ValueError("list should contain atleast two arguments.")
    if nums[0] > nums[1]:
        largest = nums[0]
        second = nums[1]
    else:
        largest = nums[1]
        second = nums[0]
    for current_number in nums[2:]:
        if current_number > largest:
            second = largest
            largest = current_number
        elif current_number != largest and current_number > second:
            second = current_number
    if second == largest:
        raise ValueError("List must contain atleast two unique element.")
    return second
#-------MAIN EXECUTION---------
if __name__ == "__main__":
    numbers_list = [12,34,5,6,7,88]
    try:
        result = second_largest(numbers_list)
    except (TypeError,ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(e)
    else:
        print("Second largest :", result)