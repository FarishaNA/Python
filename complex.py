class Complex:
    def __init__(self, real, imaginary):
        self.__real = real
        self.__imaginary = imaginary

    def __ge__(self, other):
        mag1 = (self.__real**2 + self.__imaginary**2) ** 0.5
        mag2 = (other.__real**2 + other.__imaginary**2) ** 0.5
        return mag1 >= mag2


# Example
c1 = Complex(3, 4)
c2 = Complex(1, 7)

print(c1 >= c2)
