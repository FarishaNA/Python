def arrange_lower_first(s):
    lower = "".join(c for c in s if c.islower())
    others = "".join(c for c in s if not c.islower())
    return lower + others


s = input("Enter string: ")
print(arrange_lower_first(s))
