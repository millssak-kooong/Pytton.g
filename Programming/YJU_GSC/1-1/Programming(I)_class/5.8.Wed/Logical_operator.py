value = 4

if value % 2 == 0 and value % 3 == 0:
    print("참")
else:
    print("거짓")

#______________________________________

print(bool(1)) # True
print(bool(0)) # False
print(bool(-1)) # True

#_______________________________

print(bool("fasㅇㄻ")) # True
print(bool("")) # False

#_______________________________

value = 4

if not value:
# if not bool(value):
# if not bool(4):
# if not True:
# if False:
    print("참")
else:
    print("거짓")
# False

#########################################
# Lazy evaluation

def bar(argValue):
    print("Bar is invoked")
    return argValue

if False and bar(2) == 2:
    print("참")

else:
    print("거짓")