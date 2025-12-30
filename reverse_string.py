def reverse_string(text):
    rev = ""
    for ch in text:
        rev = ch + rev
    return rev

print(reverse_string("Himanshu"))
