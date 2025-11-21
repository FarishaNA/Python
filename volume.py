class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height

    # Overload <= operator
    def __le__(self, other):
        return self.volume() <= other.volume()


# ---- Testing the classes ----

c1 = Cuboid(4, 5, 6)
c2 = Cuboid(3, 6, 7)

print("Volume of Cuboid 1:", c1.volume())
print("Volume of Cuboid 2:", c2.volume())

# Compare using overloaded <= operator
if c1 <= c2:
    print("Cuboid 1 has lesser or equal volume than Cuboid 2")
else:
    print("Cuboid 1 has greater volume than Cuboid 2")
