def reverse_array(nums: list) ->list:
    """Reverse An array in a list without Extra Space"""
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