class Person:
    def __init__(self, name, phno):
        self.name = name
        self.phno = phno


class Dept:
    def __init__(self, dept_name, location):
        self.dept_name = dept_name
        self.location = location


class Employee(Person, Dept):
    def __init__(self, name, phno, dept_name, location, designation, salary):
        Person.__init__(self, name, phno)
        Dept.__init__(self, dept_name, location)
        self.designation = designation
        self.salary = salary

    def give_increment(self, percent):
        """Increase salary by given percent (e.g. 10 for 10%)."""
        self.salary = self.salary * (1 + percent / 100.0)

    def display(self):
        print("---- Employee Details ----")
        print("Name:", self.name)
        print("Phone:", self.phno)
        print("Department:", self.dept_name)
        print("Location:", self.location)
        print("Designation:", self.designation)
        print("Salary: {:.2f}".format(self.salary))


# --- Example usage ---
if __name__ == "__main__":
    # Create an Employee
    emp = Employee(
        name="Alice Johnson",
        phno="9876543210",
        dept_name="IT",
        location="New York",
        designation="Software Engineer",
        salary=50000.0
    )

    print("Before increment:")
    emp.display()

    # Give 10% increment
    emp.give_increment(10)

    print("\nAfter 10% increment:")
    emp.display()
