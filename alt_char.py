def print_alternate(s, index=0):
    if index >= len(s):
        return
    
    print(s[index], end='')

    print_alternate(s, index + 2)


text = "She sells sea shells"
print_alternate(text)
