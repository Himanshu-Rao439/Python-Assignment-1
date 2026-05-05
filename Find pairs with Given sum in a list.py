def find_pairs(List: list,target: int) -> list:
    """
    Calculate the sum of all elements in a list after validating that 
    each element is an integer.

    Args:
        lst (list): A list containing elements to be summed.

    Returns:
        int: Sum of all integer elements in the list.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not an integer.
    """
    if not isinstance(target,(int,float)):
        raise TypeError("target must be a integer or float value")
    if not isinstance(List,list):
        raise TypeError("First Argument must be a list")
    if not all(isinstance(List,int) for List in List):
        raise ValueError("List must contains only integers")
    pairs = []
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i] + List[j] == target:
                pairs.append((List[i],List[j]))
    return pairs
if __name__ == "__main__":
    try:
        List = [1,2,3,4,5,6]
        target = 7
        print(find_pairs(List,target))
    except(TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)