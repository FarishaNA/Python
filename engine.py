#Create a class Engine(__power) and Wheels (__size) Derive class car(_model) from engine and wheels display the details of car using method overriding


class Engine:
    def __init__(self, power):
        self.__power = power
    
    def display(self):
        print('Engine Power  :',self.__power)

class Wheels:
    def __init__(self, size):        
        self.__size = size
    
    def display(self):
        print("Size  :",self.__size)

class Car(Engine, Wheels):
    def __init__(self, power, size, model):
        super().__init__(power)
        Wheels.__init__(self, size)
        self.__model = model
    
    def display(self):
        super().display()
        Wheels.display(self)
        print("Model  :",self.__model)

c = Car("1200cc", "16 inches", "Toyota Corolla")
c.display()