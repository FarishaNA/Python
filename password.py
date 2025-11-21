import re

password = input("Enter password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")
