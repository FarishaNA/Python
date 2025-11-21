#Create a class publisher (name) Derive a class Book (title, author) from Publisher . Derive a class Python(price , no_of_pages) from Book.Write a prgm that displays info bout a python Book . Use base class constructor invokation and method overriding

class Publisher:
    def __init__(self, name):
        self.__name = name
    
    def display(self):
        print('Publisher  :',self.__name)

class Book(Publisher):
    def __init__(self, title, author, name):
        super().__init__(name)
        self.__title = title
        self.__author = author
    
    def display(self):
        print("Title  :",self.__title)
        print("Author  :",self.__author)
        super().display()

class Python(Book):
    def __init__(self, title, author, name, price, num):
        super().__init__(title, author, name)
        self.__price = price
        self.__num = num
    
    def display(self):
        super().display()
        print("Price  : ₹",self.__price)
        print("No of pages  :",self.__num)

p = Python('Fundamentals of Python','Aysha','Nadiya',300,500)
p.display()