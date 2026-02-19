def check_leap_year(year: int) -> bool:
    """
    Check Whether a given year is a leap year.

    Conditions:
    1.Divisible By 4 and not divisible by 100
    2.Or Divisible by 400

    Args:
        year (int): year to check
    Returns:
        bool: True if leap year, False Otherwise
    raise TypeError:
        if year is not integer
    raise ValueError:
        if year is least than 1582
    """  
    if not isinstance(year,int):
        raise TypeError("Year must an integer value")
    if year < 1582:
        raise ValueError("Year must be later of 1582")
    if year >= 1582 and (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# _________MAIN EXECUTION____________
if __name__ == "__main__":
    user_input = 1583
    try:
        if check_leap_year(user_input):
            print(f"{user_input} is leap year")
        else:
            print(f"{user_input} is not a leap year")
    except (ValueError,TypeError) as e:
        print("Error :",e)
    except Exception as e:
        print("Unexpected Error:",e)