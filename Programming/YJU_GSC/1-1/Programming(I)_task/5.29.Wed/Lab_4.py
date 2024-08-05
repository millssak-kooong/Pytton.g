# for 문을 사용하여 아래 문자열 내 단어 개수를 출력하는 프로그램을 작성
# It is a great weather with you
################################

myString = "It is a great weather with you"
count = 1

for letter in myString:
    if " " == letter:
        count += 1

print("문자열 단어 개수: ", count)