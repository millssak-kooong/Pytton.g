# 변수로 올 수 있는 유일한 특수 문자는 '_'이다.
# 1을 10번 출력

x = 1

for _ in range(10):
    print(x)

#_____________________________________
# range(반복 횟수)
# range(시작값, 종료값): 시작 값은 첫 번째 증감값에 대한 적용이 가능할 때 선택
# range(시작값, 종료값, 증감값)

for value in range(5, -20, -5):
    print(value)

#############################################################
# 1 ~ 20으로 구성된 리스트를 생성
# list comprehension
# -> 리스트 내 원소 값들을 for 문을 사용하여 동적으로 생성
# [ expression for item in item_list if coditional expression ]

# 1. 내가 한 거
x = []
for _ in range(1, 21):
    x += [_]
print(x)

#_____________________________________
# 2. 교수님
bar = list()
for value in range(1, 21):
    bar.append(value)
print(bar)

#_____________________________________
# 3. 교수님
bar = [value for value in range(1, 21)] # 1 ~ 20
print(bar)

##############################################################
# 7로 초기화된 8개의 원소를 가지는 리스트를 생성하라.
# [ expression for item in item_list if coditional expression ]
# bar = [7, 7, 7, 7, 7, 7, 7]

bar = [7 for _ in range(8)]
print(bar)

#_____________________________________
# 3, 6, 9, 12, 15, 18
bar = [ value for value in range(1, 21) if value % 3 == 0 ]
print(bar)

#_____________________________________
# 아래 리스트 중 'c'가 포함한 단어만 선택해서 리스트로 구성

foo = ["abc", "dcd", "ef", "gh"]
bar = [ word for word in foo if "c" in word]
print(bar)

#_____________________________________
# 아래 리스트 중 단어의 글자 개수가 3개 이상인 단어만 선택하여 리스트로 구성

foo = ["abc", "dcd", "ef", "gh"]
bar = [ word for word in foo if 3 <= len(word)]
print(bar)

#_____________________________________
# 1 ~ 10 정수 중 홀수는 10을 곱하고 짝수는 20을 곱한 리스트를 생성하라
# 삼항 연산자: 참 if 조건식 else 거짓 -> 수식

a = [word * 10 if word % 2 != 0 else word * 20 for word in (1, 11)]
print(a)

####################################################
# Flag 깃발 사용하기
# 1

bar = ["hello", "world", "Richard"]
found_word = False # Flag 변수 -> 깃발: Boolean

for word in bar:
    if word == "world":
        print("단어를 찾았음")
        found_word = True
        break

if not found_word:
    print("단어를 찾지 못했음. 나빠또")

#___________________________________________________
# 2

bar = ["hello", "world", "Richard"]
# found_word = False # Flag 변수 -> 깃발: Boolean

for word in bar:
    if word == "world":
        print("단어를 찾았음")
#        found_word = True
        break

else:
    print("단어를 찾지 못했음. 나~~빠~~또!")