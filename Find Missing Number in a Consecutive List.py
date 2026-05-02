def find_missing_number(sample_list: list) ->int:
    """
    Find the first missing number in a list of consecutive integers.
    using adjacent difference comparison.

    Parameters:
    numbers (list1): List of integers

    Returns:
    int: The first missing number

    Raises:
    TypeError: If input is not a list or contains non-integers
    ValueError: If list has fewer than 2 elements

    """

    # validate input
    if not isinstance(sample_list,list):
        raise TypeError("Input must be a list")
    if len(sample_list) < 2:
        raise ValueError("Atleast Two Numbers Required inside list")
    if not all(isinstance(item,int) for item in sample_list):
        raise TypeError("All elements of list must be integer")
    
    sample_list = sorted(sample_list)
        
    for i in range(0,len(sample_list)-1):
        if sample_list[i+1] - sample_list[i] !=1:
            return sample_list[i]+1
            break
    else:
        return None
#-------MAIN EXECUTION--------
if __name__ == "__main__":
    sample_list = ["this"]
    try:
        print(find_missing_number(sample_list))
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)