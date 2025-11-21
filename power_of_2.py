def is_power_of_two(n):
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    return n != 0 and (n & (n - 1)) == 0

try:
    num = int(input("Enter number: "))
    print(is_power_of_two(num))
except ValueError as e:
    print("Error:", e)
