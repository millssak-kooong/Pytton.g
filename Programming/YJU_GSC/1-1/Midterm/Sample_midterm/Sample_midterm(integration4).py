# "1 ~ 100" 까지 양의 정수 중 "3" 이 포함된 정수만 출력하라

for i in range(1, 101): 
    if "3" in str(i):
        print(i)

# not in 이라는 것도 있다.
# for i in range(1, 101): 
#     if "3" not in str(i): # 3을 포함하지 않는 값
#         print(i)