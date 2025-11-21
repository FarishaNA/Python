class Person:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


class Marks:
    def __init__(self, maths, computer):
        self.maths = maths
        self.computer = computer


class Student(Person, Marks):
    def __init__(self, name, roll, maths, computer):
        Person.__init__(self, name, roll)
        Marks.__init__(self, maths, computer)

    def percentage(self):
        return (self.maths + self.computer) / 2

    def display(self):
        print("------ Student Details ------")
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Maths:", self.maths)
        print("Computer:", self.computer)
        print("Percentage:", self.percentage(), "%")
        print("Result:", "PASS" if self.percentage() >= 50 else "FAIL")
        print()


# -------- MAIN CODE --------
print("Enter details for Student 1:")
name1 = input("Name: ")
roll1 = input("Roll: ")
maths1 = float(input("Maths Marks: "))
comp1 = float(input("Computer Marks: "))
s1 = Student(name1, roll1, maths1, comp1)

print("\nEnter details for Student 2:")
name2 = input("Name: ")
roll2 = input("Roll: ")
maths2 = float(input("Maths Marks: "))
comp2 = float(input("Computer Marks: "))
s2 = Student(name2, roll2, maths2, comp2)

# Display each student
print("\n--- Student 1 ---")
s1.display()

print("--- Student 2 ---")
s2.display()

# Compare by percentage
p1 = s1.percentage()
p2 = s2.percentage()

print("------ Comparison Result ------")
if p1 > p2:
    print(f"{s1.name} has a higher percentage ({p1}%) than {s2.name} ({p2}%).")
elif p2 > p1:
    print(f"{s2.name} has a higher percentage ({p2}%) than {s1.name} ({p1}%).")
else:
    print(f"Both {s1.name} and {s2.name} have the same percentage ({p1}%).")
