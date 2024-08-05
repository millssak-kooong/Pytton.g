bar = {"name" : "seongbinY", "age" : 20, "phone" : 123-456, 100 : 200}
print(bar.keys())
#--------------------
print(bar["name"])
print(bar[100])
#--------------------
bar['email'] = "seongbinY@yju.ac.kr"
print(bar["email"])
#------------------------------------
# age가 있으면 Skip하고 없으면 추가해라.

if "email" in bar: # ['name', 'age', 'phone']
    print("True")
else:
    print("False")

if "mobile" in bar.keys(): # ['name', 'age', 'phone']
    print("True")
else:
    print("False")

######################################

# keys()   : 키 값
# values() : 데이터 값
# items()  : 키 + 데이터

bar = {"영어" : 20, "수학" : 30, "국어" : 40}
print(sum(bar.values())) # sum([20, 30, 40])

sum = 0
for record in bar.values():
    sum += record
print(sum)

for subject in bar.keys():
    print(subject, "\t", end = "")

for key, value in bar.items(): # [('영어', 20), ('수학', 30), ('국어', 40)]
    print(key, "\t", value)

for key in bar.keys(): # [('영어', 20), ('수학', 30), ('국어', 40)]
    print(key, "\t", bar[key])

#######################################
# Multi - dimensional Dictionary, 객체 구조화
# Dictionary에서 계층은 층의 개수를 의미한다.
bar = {
    "ycj" : {"name" : "정영철", "age" : 20, "etc" : {"성적" : 100, "등급" : "A"}},
    "lny" : {"name" : "이나영", "age" : 30}
}
print(bar["lny"])
print(bar["ycj"]["age"])
print(bar["ycj"]["etc"]["성적"])

for item in bar.values():
    for e in item.values():
        print(e)

std_grandes = {} # List + Dictionary
#                       이름   국어 영어 수학 총점 평균
std_grandes[240001] = ["홍길동", 10, 20, 30, 60, 30]
std_grandes[240002] = ["홍길이", 100, 200, 300, 600, 300]
std_grandes[240003] = ["홍길삼", 1000, 2000, 3000, 6000, 3000]
std_grandes[240004] = ["홍길사", {"국어" : 100, "수학" : 20, "영어" : 10}]

print(std_grandes[240004][-1]["국어"])
print(sum(std_grandes[240004][1].values()))

foo = [value for g in range(2) for value in range(3)]
# =
# for g in range(2):
#     for value in range(3):
#         value
print(foo)

foo = [[g for g in range(2)] for value in range(3)]
print(foo)