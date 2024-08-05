def contains(x, y):
    for z in x:
        if z == y:
            return True
    return False
print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))