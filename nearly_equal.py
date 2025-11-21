def nearly_equal(a, b):
    if len(a) != len(b):
        return False

    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

# Example
print(nearly_equal("cat", "bat"))
