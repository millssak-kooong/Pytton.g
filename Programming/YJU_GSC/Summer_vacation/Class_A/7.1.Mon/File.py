import os

# Relative reference
#f_handler = open(r"imgs/test.txt", "r")

# Absolute reference
f_handler = open(r"c:/myGame/imgs/test.txt", "r")

msg = f_handler.read()

print(msg)

f_handler.close()