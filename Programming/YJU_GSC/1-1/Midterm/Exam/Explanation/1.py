# 정수 5개 입력
input_1 = int(input("1번째 값을 입력하세요 : "))
input_2 = int(input("2번째 값을 입력하세요 : "))
input_3 = int(input("3번째 값을 입력하세요 : "))
input_4 = int(input("4번째 값을 입력하세요 : "))
input_5 = int(input("5번째 값을 입력하세요 : "))

# 합계 계산
sum = input_1 + input_2 + input_3 + input_4 + input_5

# 평균 계산
avg = sum / 5

# 합계, 평균 출력
print("합계: ", sum)
print("평균: ", avg)

#______________________________________________________

sum = 0

for count in range(1, 6):
    msg = str(count) + "번째 입력하세요: "
    input_value = int(input(msg))
    sum += input_value
    
    
avg = sum / 5    


# 합계, 평균 출력
print("합계: ", sum)
print("평균: ", avg)