class Person:
    def __init__(self, name, age):
        self.__name = name     # private attribute
        self.__age = age       # private attribute

    # Getter methods (optional, but good practice)
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    # Operator overloading for comparison by age
    def __gt__(self, other):     # greater than: p1 > p2
        return self.__age > other.__age

    def __lt__(self, other):     # less than: p1 < p2
        return self.__age < other.__age

    def __eq__(self, other):     # equal to: p1 == p2
        return self.__age == other.__age


# --- Using the class ---
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1 > p2)   # False
print(p1 < p2)   # True
print(p1 == p2)  # False
