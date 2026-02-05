from typing import List, Any

def remove_duplicates(data: List[Any]) -> List[Any]:

    if not isinstance(data, list):
        raise TypeError("Input must be a list")

    if len(data) == 0:
        raise ValueError("Input must not be empty")

    if len(data) == 1:
        print("List has already one element. No duplicate to remove")
        return data

    result = []
    for i in data:
        if i not in result:
            result.append(i)

    return result


# --------- MAIN EXECUTION ---------
if __name__ == "__main__":
    number_list = [100,3,5,7,89,56,43,67,3,3,100,100,33,33]
    try:
        result = remove_duplicates(number_list)
    except (TypeError, ValueError) as e:
        print("Error:", e)
    except Exception as e:
        print("Error:",e)    
    else:
        print("After removing duplicates:",result)
