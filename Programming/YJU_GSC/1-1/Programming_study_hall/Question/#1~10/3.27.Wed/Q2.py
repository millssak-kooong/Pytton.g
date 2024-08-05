# 평균 점수와 학점 등급 계산 프로그램
## 목적: 학생들의 3 과목 점수를 입력 받아 평균 점수를 계산하고 평균에 따른 학점 등급을 부여한다.
## 조건: 평균 90 이상 A, 80 이상 B, 70 이상 C, 60 이상 D, 60 미만 F


# 1. 평균 점수 구하는 함수 작성

def average(num1, num2, num3):
    score = (num1 + num2 + num3) / 3
    return score

# 2. 사용자로부터 수학, 과학, 영어 각 점수를 입력받기

mat = int(input("Put your Mathematics score: "))
sic = int(input("Put your Science score: "))
eng = int(input("Put your English score: "))

# 3. 입력 받은 점수들을 평균 계산하고, 평균 점수로 학점 등급 결정 후 출력

score_grade = average(mat, sic, eng)

if 90 <= score_grade:
    print(f"The average score_grade is {float(score_grade)}, grade is A.")
elif 80 <= score_grade < 90:
    print(f"The average score_grade is {float(score_grade)}, grade is B.")
elif 70 <= score_grade < 80:
    print(f"The average score_grade is {float(score_grade)}, grade is C.")
elif 60 <= score_grade < 70:
    print(f"The average score_grade is {float(score_grade)}, grade is D.")
else:
    print(f"The average score_grade is {float(score_grade)}, grade is F.")




#####################################################################

# <def 함수 사용 예시>
    
# def bar(a, b):
#     result = a + b
#     return result
# sum = bar(2, 3)
# print(sum)