# 세 수의 비교 - 유사성과 차이점 찾기
# 세 수의 관계 3 종류
## 1. 모든 수가 같으면 "모든 수가 같습니다."
## 2. 두 수가 같으면 "두 수가 같습니다."와 같은 두 수도 출력.
## 3. 모든 수가 다르면 "모든 수가 다릅니다. 가장 큰 수는 x입니다." x는 가장 큰 수.
##### 힌트: if 조건문의 중첩 사용으로 문제 해결이 가능 #####
##### print(). input(), int() 외에 다른 함수 사용 금지 #####

# 1. 사용자에게 3 개의 정수를 입력 받는다.

n1 = int(input("첫 번째 정수를 입력하시오."))
n2 = int(input("두 번째 정수를 입력하시오."))
n3 = int(input("세 번째 정수를 입력하시오."))

# 2. 3개의 수들을 3가지 조건으로 비교한 후 출력

## 3개의 정수가 같을 때
if n1 == n2 == n3:
    print("모든 수가 같습니다.")

## 2개의 정수가 같을 때, 두 수도 함께 출력
elif n1 == n2:
    print(f"두 수가 같습니다. ({n1}와 {n2})")
elif n1 == n3:
    print(f"두 수가 같습니다. ({n1}와 {n3})")
elif n2 == n3:
    print(f"두 수가 같습니다. ({n2}와 {n3})")

## 모든 정수가 다를 때, 최대값을 함께 출력
elif n1 > n2 and n1 > n3:
    print(f"모든 수가 다릅니다. 가장 큰 수는 {n1}입니다.")
elif n2 > n1 and n2 > n3:
    print(f"모든 수가 다릅니다. 가장 큰 수는 {n2}입니다.")
else:
    print(f"모든 수가 다릅니다. 가장 큰 수는 {n3}입니다.")