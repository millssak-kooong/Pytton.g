# 사칙연산 계산기 - 전역변수와 지역변수 사용
## 초기값(baseValue)을 입력받아 전역 변수로 선언할 것
## 프로그램은 더하기, 빼기, 곱하기, 나누기 중 하나의 연산을 수행할 것
## 연산을 선택하고 숫자를 입력하면, selectOperation() 함수에서 선택한 연산을 baseValue에 적용할 것
## selectOperation() 함수는 전역 변수 baseValue를 참조하여 연산을 실행할 것
## 나누기 연산에서 분모가 0일 경우, "에러: 0으로 나눌 수 없습니다."라는 메시지를 출력하고 결과는 출력하지 말 것.
## 에러 메시지가 출력되지 않은 경우에만 연산 결과를 출력할 것.

# 1. 초기값 baseValue 값을 입력 받는다.

baseValue = float(input("기본값을 입력하세요: "))

# 2. 연산자의 선택지를 보여 주고 하나를 선택 받는다.

print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")
inputOperation = input("연산자 선택: ")

# 3. 함수 작성!

def selectOperation():
    if inputOperation == "1":
        return baseValue + inputNum
    elif inputOperation == "2":
        return baseValue + inputNum
    elif inputOperation == "3":
        return baseValue * inputNum
    elif inputOperation == "4":
        if inputNum == 0: # 나눗셈을 할 시 분모가 되는 inputNum은 0이 될 수 없음을 출력
            return "에러: 0으로 나눌 수 없습니다."
        else:
            return baseValue / inputNum
    else: # 선택지에 없는 연산자 번호를 입력했을 때
        return "메뉴에 없는 연산자입니다!"
     
# 4. 연산 할 나머지 숫자를 입력 받는다.

inputNum = float(input("숫자 입력: "))

# 4. 연산 결과를 출력한다.

result = selectOperation()
print(result)