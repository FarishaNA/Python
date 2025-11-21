#4.	Write a program to print all even numbers from a given list in the given order until you reach number 237 or end of the list.

l1 = list(map(int, input("Enter the list").split()))

def even_until237(l1):
    evn = []
    for n in l1:
        if n == 237:
            break
        elif not n % 2:
            evn.append(n)
    return evn



