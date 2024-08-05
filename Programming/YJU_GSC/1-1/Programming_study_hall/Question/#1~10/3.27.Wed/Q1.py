# <면적 단위 변환기>
# 사용자가 제곱미터(m^2) 단위로 입력한 토지의 면적을 평방피트(ft^2)와 에이커(ac) 단위로 변환해주는 프로그램을 작성하세요. 변환 공식은 다음과 같습니다
## 1제곱미터 (m^2) = 10.7639 평방피트 (ft^2)
## 1에이커 (ac) = 4046.86 제곱미터 (m^2)


# 1. 변환 함수 코드 작성
## 2 개의 함수를 정의하여 각 단위로의 변환을 담당합니다.

def convert_to_square_feet(square_meters): # convert_to_square_feet: 제곱미터를 평방피트로 변환
    return square_meters * 10.7639 # 제곱미터를 평방피트로 변환하는 공식 작성

def convert_to_acres(square_meters): # convert_to_acres: 제곱미터를 에이커로 변환
    return square_meters / 4046.86 # 제곱미터를 에이커로 변환하는 공식 작성

# 2. 토지의 면적을 제곱미터(m^2) 단위로 입력 받는다.

square_meters = int(input("토지의 면적을 제곱미터(m^2) 단위로 입력하세요: "))
    
# 3. 면적을 평방피트(ft^2)와 에이커(ac)로 변환합니다.
## 입력받은 면적이 음수일 경우, 변환 대신 "잘못된 입력입니다"를 출력합니다.
## if 선택문을 활용합니다.

if square_meters < 0:
    print("잘못된 입력입니다")

else :
    a = (float(square_meters), "제곱미터는", float(convert_to_square_feet(square_meters)), "평방피트입니다.")
    b = (float(square_meters), "제곱미터는", float(convert_to_acres(square_meters)), "에이커입니다.")