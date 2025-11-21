#Accept a list of single digit numbers as input string. Concatenate the elements of the list as a single number.

def concat_digits(list1):
    nums = ""
    for num in list1:
        nums += num
    return nums


list1= list(input("Enter a list of single digit elements :").split())

print(list1)
print("Concatenated list is "+ concat_digits(list1))


