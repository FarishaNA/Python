count = int(input("Enter the number of terms :"))

f1, f2 = 0, 1
print(f1)
print(f2)
for i in range(count -2):
    f1 , f2 = f2, f1+f2
    print(f2)

num = int(input("Enter the term to print :"))

if num == 1:
   print(0)
elif num == 2:
    print(1)
elif num > 2:
    f1 , f2 = 0, 1
    for i in range(num -2):
       f1 , f2 = f2, f1+f2
    print("The ",num,"th term is ",f2)
else:
    print("Invalid term")