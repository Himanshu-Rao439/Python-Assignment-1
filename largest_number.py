def largest_number(lst):
    # Step 1: check if list is empty
    if len(lst) == 0:
        return "List is empty"

    # Step 2: initialize index
    i = 0

    # Step 3: assume first element is the largest
    largest = lst[0]

    # Step 4: traverse the list using while loop
    while i < len(lst):
        if lst[i] > largest:
            largest = lst[i]   # update largest
        i += 1                 # move to next index

    # Step 5: return the largest number
    return largest


# ----------- MAIN PROGRAM -----------

numbers = [10, 45, 3, 99, 23]

result = largest_number(numbers)

print("List:", numbers)
print("Largest number in the list is:", result)
