# Dictionary_data_structure는 학문이다. 데이터를 어떻게 보관하고 관리할 거냐에 대한 것.
## 자료 구조는 이론 또는 방법이다.
### 어떤 식으로 구현할지 만든 게 collection.
#### Python 내장 컬랙션: List(index), Tuple(immutable), Dictionary(key-value), Set(unique)

# 프로그램은 알고리즘과 데이터로 구성된다. 데이터는 변수가 되고 알고리즘은 명령어들의 순서와 절차이다.

# Primitive types: 원시는 하나의 변수

# Composite types(Non_primitive type): Array 배열과 linked_list

# Abstract data types: 두 개 이상의 변수를 어떻게 묶을 것이냐
# 우리가 배운 것들 모두 

bar = [10, 20] # List 생성 [ ]

foo = (30, 40) # Tuple 생성 ( )

print(bar[0], foo[0]) # 10, 30

bar[0] = 100 # Mutable
foo[0] = 200 # Immutable

############################
bar = []

for _ in range(5):
    bar.append(input("값: "))

print(bar)

# --------------------------

kin = []

for _ in range(5):
    kin.insert(0, input("값: "))

print(kin)

# --------------------------

foo = set()

for _ in range(5):
    foo.add(input("값: "))

print(foo)

############################
import random

bar = [random.randint(1, 7) for _ in range(10)]
print(bar)

foo = set()

for index in range(10):
    foo.add(bar[index])

print(foo)

############################
# Dictionary[Map]는 언제 쓴다? 데이터 검색과 접근이 빈번할 때.
# bar = {"x", "y", "z"} # index가 0부터 정수가 아닌 원하는 Key로 저장하여 Value와 fair하게 저장할 수 있다.
## Hash Function을 통해 key를 저장하여 바로바로 찾아 준다.
## Data는 중복 가능하나 Key는 유일해야 한다.

bar = {}

print(type(bar))

bar["ycj"] = "정영철"

print(bar["ycj"])

foo = [10, 20, 3, 5, 6, 200, 300]

for value in foo:
    if value == 300:
        print("300이 리스트 내 있습니다.")