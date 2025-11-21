#3.	Write a program to search an item in a given list and display the number of occurrences of the given item. 

def search(num, lst):
    count = 0
    for n in lst:
        if n == num:
            count += 1
    return count

lst = list(map(int,input("Enter the list :").split()))
num = int(input("Enter the number to search :"))
print(f"Count of {num} is {search(num, lst)}")