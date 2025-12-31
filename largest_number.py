def largest_number(lst):
    i = 0                 # index start
    largest = lst[0]      # assume first number is largest

    while i < len(lst):   # jab tak list khatam na ho
        if lst[i] > largest:
            largest = lst[i]
        i += 1            # next index

    return largest


numbers = [10, 45, 3, 99, 23]
print(largest_number(numbers))

