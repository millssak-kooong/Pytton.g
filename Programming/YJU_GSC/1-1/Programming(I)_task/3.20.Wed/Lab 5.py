# [키보드로부터 입력받은 한글 성별을 영어로 변환]

# 1. 사용자로부터 "남자" 또는 "여자"라는 문자열 입력받기

MW = input("성별을 한글로 입력하세요 (남자/여자): ")

# 입력된 문자열이 "남자"인 경우 "MAN"으로 변환하여 출력

if MW == "남자":
    print("MAN") # MW가 남자라면 "MAN"을 출력한다.

# 입력된 문자열이 "여자"인 경우 "WOMAN"으로 변환하여 출력
    
elif MW == "여자":
    print("WOMAN") # MW가 "여자"라면 "WOMAN"을 출력한다.

# 이외의 입력에 대해서는 오류 메시지 출력한다.

else:
    print("잘못된 입력입니다.") # MW가 "남자" 또는 "여자"가 아니라면 "잘못된 입력입니다."를 출력한다.