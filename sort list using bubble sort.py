def sort_list(my_list: list) -> list:
    """
    Sort a list of integers in ascending order using the bubble sort algorithm.

    Parameters:
    list1 (list): A list containing only integers.

    Returns:
    list: The sorted list in ascending order.

    Raises:
    TypeError:
        -if the input is not a list.
        -if any element in the list is not an integer.
    """
    if not isinstance(my_list,list):
        raise TypeError("input must be a list of integers")
    for item in my_list:
        if not isinstance(item,int):
            raise TypeError("All elements of list should be integer")
    length = len(my_list)
    for i in range (length):
        for j in range (0,length-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
    return my_list
if __name__ == "__main__":
    my_list = [96,68,93,55,86,42,37,92,87,50]
    try:
        print(sort_list(my_list))
    except TypeError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)