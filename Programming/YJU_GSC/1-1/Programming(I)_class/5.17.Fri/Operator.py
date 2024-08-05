# is, is not -> Identity operator

bar = [2, 4, 5]
foo = [2, 4, 5]
# 0xaa == 0xab
if bar is foo:
    print("참")
else:
    print("거짓")

#_____________________________________________
# 삼항(Ternary) 연산자

msg = ""
value = 1

if value == 1:
    msg = "안녕"
else:
    msg = "hello"

# 삼항 연산자 -> "안녕" if value == 1 else "hello"
msg = "안녕" if value == 1 else "hello"


#__________________________________________________

strike_out = True

print("패배" if strike_out else "승리")

if strike_out:
    print("패배")
else:
    print("승리")