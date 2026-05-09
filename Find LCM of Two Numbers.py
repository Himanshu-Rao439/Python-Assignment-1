num1 = "th9os"
num2 = "htiodl"

def lcm_finder(a: int,b: int) -> int:
    """This Function provide lcm of two numbers"""
    if not isinstance(num1,int) or not isinstance(num2,int):
        raise TypeError("Both Values should be integers")
    if num1 == 0 or num2 == 0:
        raise ValueError("LCM is not Defined for zeros")
    
    def gcd(a,b):
        while b != 0:
            a,b = b,a%b
        return a
    return abs(a*b)//gcd(a,b)
if __name__ == "__main__":
    num1 = 12
    num2 = 36
    try:
        print(lcm_finder(num1,num2))
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)