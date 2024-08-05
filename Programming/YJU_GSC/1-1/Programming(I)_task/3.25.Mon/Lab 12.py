# 함수 구현 - 개인 소득세(Personal Income Tax) 계산 프로그램
## 이 프로그램은 사용자로부터 소득 금액을 입력받아 소득세를 계산한다.
### 첫 1만 달러의 소득(income)에는 10%의 세율이 적용됨
### 1만 달러를 초과하고 2만 달러 이하의 소득에 대해서는 초과 금액에 15%의 세율을 적용하고, 첫 1만 달러의 세금인 1천 달러를 더한다.
### 2만 달러를 초과하는 소득에 대해서는 초과 금액에 20%의 세율을 적용하고, 앞선 구간의 세금인 2천 5백 달러를 더한다.


# 1. 소득세 계산 함수를 작성한다.

def calculate_tax(income):
    if income <= 10000:
        return (income * 0.1)
    
    elif 10000 < income <= 20000:
        return ((income - 10000) * 0.15) + 1000

    else:
        return ((income - 20000) * 0.2) + 2500

# 2. 소득 금액을 입력 받는다.

user_income = int(input("소득 금액을 입력하세요: "))

# 3. 계산된 소득세를 출력한다.

print(f"소득세는 {float(calculate_tax(user_income))}달러입니다.")