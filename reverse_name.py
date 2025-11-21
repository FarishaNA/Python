#1.	Accept full name and display in reverse order with space between the words.
def name_reverse(name):
    reversed_name = name[::-1]
    return reversed_name

name = input("Enter your full name: ").split()
print(" ".join(name_reverse(name)))
