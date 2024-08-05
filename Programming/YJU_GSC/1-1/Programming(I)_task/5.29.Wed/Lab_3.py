# for 문을 사용하여 아래 문자열 내 'h' 글자 개수 구하기
# hello hyundai hoho
####################################################

myString = "hello hyundai hoho"
count = 0

for letter in myString:
    if "h" == letter:
        count += 1
        
print("문자열 내 h 개수: ", count)