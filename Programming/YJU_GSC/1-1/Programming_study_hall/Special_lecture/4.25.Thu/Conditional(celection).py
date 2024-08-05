input_value = int(input("성적 입력: "))

go = ""


if input_value >= 90:
    go = "A"
elif input_value >= 80:
    go = "B"
elif input_value >= 70:
    go = "C"
elif input_value >= 60:
    go = "D"
else:
    go = "F"


go += "등급"
print(go)