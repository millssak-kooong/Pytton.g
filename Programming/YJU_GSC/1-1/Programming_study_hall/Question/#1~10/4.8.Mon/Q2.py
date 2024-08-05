# 리스트에서 항목 읽기
## 친구들과 메뉴를 정하는 프로그램
## 정해진 메뉴 리스트가 있고 사용자에게 인덱스 번호를 받아 해당 메뉴 출력
### 만약 유효하지 않은 인덱스 입력하면 "유효하지 않은 선택입니다"를 출력

# 1. Defined lunch menu list

menu = ["피자", "파스타", "샐러드", "스시", "버거"]

# 2. Get the index number from user.

indexNum = int(input("메뉴의 인덱스 번호를 입력하시오. (0부터 시작): "))

# 3. Print a menu what user inputted of index number.

if 0 <= indexNum <= 4:
    print("선택된 메뉴:", menu[indexNum])

# 4. If an unvalied num, then print "유효하지 않은 선택입니다".

else:
    print("유효하지 않은 선택입니다")