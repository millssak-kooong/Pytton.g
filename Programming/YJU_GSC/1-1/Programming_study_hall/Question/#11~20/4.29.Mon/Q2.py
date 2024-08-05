# 명시적 형변환 Explicit type conversion
# 사용자로부터 여러 개의 숫자를 문자열로 입력 받는다.(예: "5, 20, 15, 60")
# 문자열을 개별 숫자로 분리하고,
# 각 숫자를 정수로 변환 후 모든 숫자 합을 계산
# 숫자의 총합이 100 초과면 해당 순간의 입력 값들과 총합을 출력하고 프로그램 종료.
# 숫자의 총합이 100을 초과하지 않은 경우 최종 총합과 입력된 숫자들을 출력

# 1. 숫자들을 문자열로 입력 받기

nums_str = input("숫자들을 쉼표로 구분하여 입력하세요: ")
# 문자열을 숫자 리스트로 변환
nums = nums_str.split(',')
list = []
sum = 0

for x in nums:
    num = int(x)
    sum += num
    list.append(num)
    print(sum)
    print(list)


#____________________________________________
# 교수님 풀이

input_num_list = input("숫자를 입력하세요: ")

num_list = input_num_list.split(",")

sum = 0
output_list = []
over_100_flag = False

for num_str in num_list:
    num = int(num_str)
    sum += num
    output_list.append(num)

    if sum > 100:
        over_100_flag = True
        break
if over_100_flag:
    print("100 초과", sum)
    print(output_list)
else:
    print("100 이하", sum)
    print(output_list)