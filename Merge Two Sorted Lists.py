def merge_sorted_list(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Args:
        list1 (list): First sorted list of elements.
        list2 (list): Second sorted list of elements.

    Returns:
        list: A new list containing all elements from list1 and list2 in sorted order.

    Raises:
        TypeError: If either list1 or list2 is not a list.
                   If elements inside the lists are not comparable (e.g., mixed data types).
    """
    if not isinstance(list1,list) or not isinstance(list2,list):
        raise TypeError("Both Inputs must be lists")
    for item in list1 + list2:
        if not isinstance(item,(int,float)):
            raise TypeError("Lists must contain only numbers")
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    # remaining elements
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list
if __name__ == "__main__":
    list1 = [4,34,56,78,90,7000,8000,]
    list2 = [3,56,78,90,1000,4000,5000,6000,]
    try:
        print(merge_sorted_list(list1,list2))
    except Exception as e:
        print(e)