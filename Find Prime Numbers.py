def is_prime_number(n):
    if n <= 1:
        return False

    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False

    return True


if __name__ == "__main__":
    try:
        prime_number = []

        lower_limit = input("Enter lower limit : ")
        upper_limit = input("Enter upper limit : ")

        if not lower_limit.strip().isdigit():
            raise TypeError("Lower limit must be a valid integer.")

        if not upper_limit.strip().isdigit():
            raise TypeError("Upper limit must be a valid integer.")

        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)

        for i in range(lower_limit, upper_limit):
            if is_prime_number(i):
                print(f"{i} prime number")
                prime_number.append(i)

        print("Prime Numbers List:", prime_number)

    except (TypeError, ValueError) as e:
        print(e)

    except Exception as e:
        print(e)