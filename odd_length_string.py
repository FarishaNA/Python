def middle_three(s):
    if len(s) <= 7 or len(s) % 2 == 0:
        return "Invalid string"
    mid = len(s) // 2
    return s[mid-1 : mid+2]


text = "programming"
print(middle_three(text))
