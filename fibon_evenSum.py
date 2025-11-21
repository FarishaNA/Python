def sum_even_fib(n):
    a, b = 0, 1
    total = 0
    while a <= n:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

print(sum_even_fib(100))
