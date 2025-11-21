num = int(input("Enter a number :"))

if num >= 0:
   fact = 1
   for i in range(1,num + 1):
      fact *= i
   print("Factorial is ",fact)
else:
   print("Number must be greater than 0")
      