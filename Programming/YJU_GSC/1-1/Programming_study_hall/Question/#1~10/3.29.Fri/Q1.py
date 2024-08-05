# <가상 주식 거래 시뮬레이션>
## 사용자는 초기 자본금 으로 주식을 구매하고 가격 변동 이후 판매하여 발생하는 손실을 계산한다.
### 주식 구매 비용 계산: 구매 가격 * 구매 주식 수
### 남은 자본금 계산: 초기 자본금  - 총 구매 비용
### 판매 예상 이익 또는 손실 계산: (판매할 때 주식 가격 * 구매했던 주식 수) - 총 구매 비용
### 결과 출력: 구매 후 남은 자본금과 예상 이익 또는 손실
### 예시 입력값: 초기 자본금(10000), 주식 구매 가격(100), 구매 주식 수(50), 판매 주식 가격(150)
#____________________________________________________________________________

# 1. 주식 놀이에 필요한 함수와 매개 변수 Parameter vriable 작성

def play_stock(asset, price_of_buy_stock, the_number_of_buy_stock, price_of_sell_stock): # 주식 투자와 손익 계산하는 공식 작성
    cost_of_buy_stock = price_of_buy_stock * the_number_of_buy_stock # 주식 총 구매 비용 공식 작성
    last_asset = asset - cost_of_buy_stock # 주식 구매 후 남은 자본 계산 공식 작성
    pros_or_cons = (price_of_sell_stock * the_number_of_buy_stock) - cost_of_buy_stock # 손익 금액 계산 공식 작성
    print(f"구매 후 남은 자본금: {float(last_asset):.2f}") # 투자 후 남은 자본 출력
    print(f"예상 이익: {float(pros_or_cons):.2f}") # 투자 후 예상 손익 금액 출력
    if pros_or_cons < 0: # 투자가 손실일 때 출력문
        print("예상되는 손실입니다.")
    elif pros_or_cons == 0: # 투자가 원금 회수일 때 출력문
        print("원금 회수")
    else: # 투자가 이득일 때 출력문
        print("예상되는 이익입니다.")

# 2. 주식 놀이에 필요한 사용자의 인자값 Argument들 받아 내기

input_asset = int(input("초기 자본금을 입력하세요: "))
input_price_of_buy_stock = int(input("구매할 주식 가격을 입력하세요: "))
input_the_number_of_buy_stock = int(input("구매할 주식 수를 입력하세요: "))
input_price_of_sell_stock = int(input("판매할 때의 주식 가격을 입력하세요: "))

# 3. 주식 놀이를 실행한다.

play_stock(input_asset, input_price_of_buy_stock, input_the_number_of_buy_stock, input_price_of_sell_stock)