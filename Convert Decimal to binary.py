def decimal_to_binary(decimal: int) -> str:
    """
    Convert a decimal number to its binary representation.

    Args:
        decimal (int): Decimal number

    Returns:
        str: Binary representation
    """
    if not isinstance(decimal,int):
        raise TypeError("Input should be integer only")
    if decimal == 0:
        return "0"   
    binary = "" 
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary
#-----MAIN EXECUTION------
if __name__ == "__main__":
    decimal = 128
    try:
        result = decimal_to_binary(decimal)
        print(result)
    except TypeError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)