list1 = list(map(int, input("Enter list elements :").split()))

if len(list1) == 0:
    print("Empty list")
else:
    print("Sum is ",sum(list1))


