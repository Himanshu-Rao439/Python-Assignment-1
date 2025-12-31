largest_number.py
def largest_number(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

numbers = [10, 45, 3, 99, 23]
print(largest_number(numbers))