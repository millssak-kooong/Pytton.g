# 리스트에 항목 추가하기
## 학교 도서관에 사용자가 입력하는 도서 제목을 프로세스 종료할 때까지 도서 목록에 추가하는 기능을 반복
## 종료라고 입력하면 전체 도서 목록을 출력하고 종료

# 1. 사용자에게 도서 이름을 받아내거나 종료할지 묻기
## 사용자가 종료할 때까지 반복해야 함

book = [] # 책들을 나열하는 코드 작성


while True:
    title = input("What is the name of the book? If you want to stop the program, input '종료'. : ")
    if title == "종료":
        break
    book.append(title)
    
# 2. 사용자가 종료를 할 시 모든 도서 이름 출력 후 종료

print("Book list: ", book)