def sort_dict_by_value(data):
    """Function for Sort Dictionary by Key"""
    if not isinstance(data,dict):
        raise TypeError("input must be a dictionary")
    if data == {}:
        raise ValueError("data cannot be empty")
    return sorted(data.items(),key = lambda x:x[1],reverse=False)

if __name__ == "__main__":
    data = {"apple":5,"banana":2,"cherry":8,"date":3}
    try:
        print(sort_dict_by_value(data))
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)