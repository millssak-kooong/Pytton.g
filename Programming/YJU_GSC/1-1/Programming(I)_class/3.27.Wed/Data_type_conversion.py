# # Truthy, Falsy 예제

############################################

# temp_1 = 1
# temp_2 = -1
# temp_3 = 0
# temp_4 = -0

# if temp_1:
#     print("참")
# else:
#     print("거짓")
    
# if temp_2:
#     print("참")
# else:
#     print("거짓")

# if temp_3:
#     print("참")
# else:
#     print("거짓")

# if temp_4:
#     print("참")
# else:
#     print("거짓")

# ###################################

# temp_1 = 0
# temp_2 = 0.0
# temp_3 = ""
# temp_4 = None

# if temp_1:
#     print("참")
# else:
#     print("거짓")
    
# if temp_2:
#     print("참")
# else:
#     print("거짓")

# if temp_3:
#     print("참")
# else:
#     print("거짓")

# if temp_4:
#     print("참")
# else:
#     print("거짓")

# ########################################
# # " " -> 공백도 문자로 인식
# # ""는 Falsy
# inputValue = input("글자를 입력하세요")

# if inputValue:
#     print("참 입니다")
# else:
#     print("거짓 입니다")

######################################
    
# # Type casting (형변환): 문자열(str) -> 정수형(int)

# inputValue1 = input("첫 번째 숫자를 입력하세요")
# print(type(inputValue1))

# inputValue1 = int(inputValue1)

# print(type(inputValue1))

#############################################

# # 정수 변환, 문자열 -> 정수
# user_input = "10"
# converted_input = int(user_input)
# print(converted_input + 5) # 출력: 15

# # 실수 변환, 문자열-> 실수
# str_number = "3.14"
# pi = float(str_number)
# print(pi * 2)

#############################################
# # 형변환을 할 수 없는 경우

# bar = "ff12fff"
# foo = int(bar)
# print(bar, foo) # erro가 뜬다.

#############################################

# bar = 2
# foo = 3
# pos = 4
# print(bar, foo, pos)

# count = 1
# while count <= 100000000: # 실행 다 되는 데 몇 초 정도 걸린다. 
#     count = count + 1
# print("프로그램 종료")

# # bar 변수의 접근번위는?
# # 접근 범위: 시작, 끝
# # 시작: 99라인 이후
# # 끝: 프로그램의 제일 마지막 라인까지

###########################################################

# bar = 2
# del bar # 메모리를 해제하는 명령어
# print(bar)