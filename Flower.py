class Flower:
    def __init__(self, name):
        self.name = name

    def display(self):
        if hasattr(self, "petalColor"):
            print(f"{self.petalColor} {self.name}")
        else:
            print("Unknown Flower")

# Example
f = Flower("Rose")
f.petalColor = "Red"
f.display()
