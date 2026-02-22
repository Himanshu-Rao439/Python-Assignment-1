def calculate_power(base_value: int, power_value:int) -> int:
    """
    Calculate power of a number without using ** operator.

    Args:
        base_value (int): Base number
        power_value (int): Power (must be non-negative)

    Returns:
        int: base_value raised to the power_value

    Raises:
        ValueError: If power_value is negative
        TypeError:  if base_value or power_value is not an integer

    """    
    if not isinstance(base_value,int) or not isinstance(power_value,int):
        raise TypeError("Both base_value and power_value must be an integer")
    if power_value < 0:
        raise ValueError("Power Must be a positive number")
    result = 1
    for i in range(power_value):
        result = result * base_value
    return result        
# _____MAIN EXECUTION____
if __name__ == "__main__":
    base_value = 8
    power_value = 3
    try:
        print(calculate_power(base_value,power_value))
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)