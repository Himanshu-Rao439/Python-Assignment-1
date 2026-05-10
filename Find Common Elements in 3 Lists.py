def find_common_element(list1: list,list2: list,list3: list) -> list:
    """Returns a list of elements common in all three lists without sets"""
    if not isinstance(list1,list) or not isinstance(list2,list) or not isinstance(list3,list):
        raise TypeError("all elements must be lists")
    common = []
    for item in list1:
        if item in list2 and item in list3 and item not in common:
            common.append(item)
    return common
if __name__ == "__main__":
    list1 = [1,2,3,78,4,5,5,2,3]
    list2 = [3,4,5,6,7,78]
    list3 = [5,6,7,8,9,78]
    try:
        print(find_common_element(list1,list2,list3))
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)