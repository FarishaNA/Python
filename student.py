
# Create class Person (name, roll) and Marks (Maths, Computer). Create class Student from Person and Marks. Display student details and pass/fail, if 50% is needed for a pass.

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

    def display(self):
        total = self.maths + self.computer
        percentage = total / 2

        print("------ Student Details ------")
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Maths Marks:", self.maths)
        print("Computer Marks:", self.computer)
        print("Total:", total)
        print("Percentage:", percentage, "%")

        if percentage >= 50:
            print("Result: PASS")
        else:
            print("Result: FAIL")


# --------- MAIN CODE ----------
name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
maths = float(input("Enter Maths Marks: "))
computer = float(input("Enter Computer Marks: "))

s = Student(name, roll, maths, computer)
s.display()
