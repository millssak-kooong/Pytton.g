# List creation and insert
## 순차적으로 코드 작성할 것
### 1. shopping_list라는 이름의 빈 리스트를 생성
### 2. 리스트에 milk, bread, eggs, apple를 추가한다.
### 3. print 함수를 사용하여 현재 쇼핑 리스트의 내용을 출력
### 4. 쇼핑 리스트에 toilet paper를 맨 앞에 추가
### 5. orange juice를 리스트의 두 번째 위치에 추가
### 6. chiken, rice를 리스트에 추가하는데 한 번의 연산으로 추가(extend()함수 또는 '+' 연산 사용)
### 7. 쇼핑 리스트를 출력하여 추가된 품목들 확인

# 1. 빈 쇼핑 리스트 만들기

shopping_list = []

# 2. 쇼핑 리스트에 milk, bread, eggs, apple를 추가

shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.append("apple")

# 3. 현재 쇼핑 리스트 출력

print(shopping_list)

# 4. 쇼핑 리스트에 toilet paper 맨 앞에 추가

shopping_list.insert(0, "toilet_paper")

# 5. orange_juice를 리스트 두 번째에 추가

shopping_list.insert(1, "orange_juice")

# 6. chiken, rice를 리스트에 한 번의 연산으로 추가

shopping_list.extend(["chiken", "rice"])

## shopping_list += "chicken", "rice" # 또 다른 방법

# 7. 최종 쇼핑 리스트 출력

print(shopping_list)