def reverse_integer(num: int) -> int:
    """
    Reverse a string with Best approach method using loop.
    
    Args:(integer Value).

    Returns: Integer.

    TypeError: Input must a integer.
    
    """  
    if not isinstance(num,int):
        raise TypeError("input must be a integer")
    sign = -1 if num < 0 else 1
    num = abs(num)
    reversed_num = 0
    while num > 0:
        digit = num%10
        reversed_num = reversed_num * 10 + digit
        num = num//10
    return sign*reversed_num
if __name__ == "__main__":
    num = 1234
    try:
        result = reverse_integer(num)
        print("Reverse Number:",result)
    except TypeError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)