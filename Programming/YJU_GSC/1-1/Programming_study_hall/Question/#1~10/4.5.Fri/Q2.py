# 대한민국 주민번호 유효성 검사기
## 주민번호는 총 13자리 숫자로 구성
## 앞의 6자리는 생년월일을 나타내며, 뒤의 7자리는 성별, 출생등록지, 일련번호 및 검증번호로 구성됨
## 사용자의 주민번호를 입력 받아, 주민번호의 유효성을 검사

# 1. 사용자의 주민번호를 입력 받는다.

text = input("주민번호를 입력하세요: ")

# 2. 유효성을 검사를 위해 각 자리수를 하나하나 공식에 맞게 계산하는 코드 작성

for character in text[0]:
    num1 = int(character)

for character in text[1]:
    num2 = int(character)

for character in text[2]:
    num3 = int(character)

for character in text[3]:
    num4 = int(character)

for character in text[4]:
    num5 = int(character)

for character in text[5]:
    num6 = int(character)

for character in text[6]:
    num7 = int(character)

for character in text[7]:
    num8 = int(character)

for character in text[8]:
    num9 = int(character)

for character in text[9]:
    num10 = int(character)

for character in text[10]:
    num11 = int(character)

for character in text[11]:
    num12 = int(character)

# 3. 유효성 검사를 위해 계산된 각 자리수의 값들을 남은 검사 계산 절차에 맞게 계산한다.
## 각 자리수의 값들을 모두 더한다.

sum = num1 * 2 + num2 * 3 + num3 * 4 + num4 * 5 + num5 * 6 + num6 * 7 + num7 * 8 + num8 * 9 + num9 * 2 + num10 * 3 + num11 * 4 + num12 * 5

## 더한 값을 마지막 계산식에 때려 박는다.

calculation1 =  11 - (sum % 11)
# print(type(calculation1))
# 여기서부터 결과값이 제대로 안 나옴
# 4. 유효성 검사를 위한 계산을 마친 값을 유효한지 검사를 해 보고 출력한다.

if 10 <= calculation1: # 검사 값이 두 자리일 때
    if calculation1[1] == text[12]:
        print("유효한 주민번호입니다.")
    else:
        print("유효하지 않은 주민번호입니다.")
else: # 검사 값이 한 자리일 때
    if calculation1[0] == text[12]:
        print("유효한 주민번호입니다.")
    else:
        print("유효하지 않은 주민번호입니다.")

##############################################################################
# 4.12.금 - 해설 때 교수님 풀이
input_number = input("문자열을 입력하세요: ")
check_number = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

# 유효성 검사

# 주민번호 12자리를 자리별 체크 값과 곱한 후 더한다.
# 주민번호 12자리: 0 번째 index -> 11번째 index
sum = 0
count = 0
for num in input_number:
    if num != "-" and count < 12:
        sum += int(num) * check_number[count]
        count += 1

# 체크값을 계산한다 : (11-(sum % 11)) % 10 == input_number[-1]
check_value = (11 - (sum % 11)) % 10

# 판별 결과 값을 출력한다.
if check_value == int(input_number[-1]):
    print("유효한 주민번호")
else:
    print("유효하지 않은 주민번호")

#################################################################
# 2024.06.07.금 - 성공

formula = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
num_box = []
num = input("주민번호를 입력하세요: ")

for x in num:
    num_box += x
del num_box[6] # num_box.remove("-")도 가능
last_num = num_box.pop(12) # 주민번호 끝자리 잠깐 지우기
#----------------------------------------- 주민번호의 숫자들만 뽑아서 리스트로 정렬
count = 0
sum = 0
for y in formula:
    mul = int(y) * int(num_box[count])
    sum += mul
    count += 1

z = 11 - (sum % 11)

if z >= 10:
    z - 10
    if z == int(last_num):
        print("유효한 주민번호입니다.")
    else:
        print("유효하지 않은 주민번호입니다.")
else:
    if z == int(last_num):
        print("유효한 주민번호입니다.")
    else:
        print("유효하지 않은 주민번호입니다.")



# 790608-2552416
# 040425-2454578
######################################################
# 2024.06.08.Saturday.Success
#____________________________
# # 790608-2552416 = Valid
# 040425-2454578 = Invalid
# Calculation list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
#________________________________________________________

# 1. 사용자 주민번호 작업
id_num = input("Give me your ID num: ")
id_box = []
for x in id_num:
    id_box.append(x)
id_box.remove("-")
secret_num = int(id_box.pop())
pass # print(id_box)

# 2. 주민번호 한 자리씩 계산 작업
extra_num = 0
sum = 0
formula = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
for y in formula:
    sum += y * int(id_box[extra_num])
    extra_num += 1
pass # print(sum)

# 3. 최종 검사 작업
if (11 - sum % 11) % 10 == secret_num:
    print("Valid")
else:
    print("Invalid")