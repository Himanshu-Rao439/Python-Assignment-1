def is_armstrong(number: int) -> bool:
    """This Function tells whether a number armstrong or not"""
    if not isinstance(number,int):
        raise TypeError("number must be a integer value")
    if number == 0:
        raise ValueError("inputs should be contains only numeric values")
    temp_copy = number
    digit_count = 0
    while temp_copy > 0:
        digit_count = digit_count + 1
        temp_copy = temp_copy//10
    # print(digit_count)
    total = 0
    temp_copy = number
    while temp_copy > 0:
        digit = temp_copy % 10
        total = total + digit ** digit_count
        temp_copy = temp_copy // 10
    return total == number

#------MAIN EXECUTION-----
if __name__ == "__main__":
    number = 153
    try:
        print(is_armstrong(number))
    except(TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)