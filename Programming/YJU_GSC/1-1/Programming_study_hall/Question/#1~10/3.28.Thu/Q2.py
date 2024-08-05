# 출석 점수 프로그램
# # 영진전문대학에서는 출석 점수 만점을 20점으로 설정하고 있으며, 다음 기준에 따라 점수를 산정합니다.
# ## 출석 점수 계산법: 20 - (20 * 결석 시간 수 / 총 수업 시간 수)
# ## 총 수업 시간 계산법: 일주일의 수업 시간 * 15
# ## 지각 처리 규칙: 지각 3회는 결석 1시간으로 처리
# ## 결석 처리 규칙: 결석 시수가 총 수업 시수의 1/4을 초과할 경우 학점 미부여(F처리)


# 1. 출석 점수 판단 함수 작성
def attendance_score(hpw, ah, tc):
    if (ah + (tc / 3)) > ((hpw * 15) / 4): # 결석 시간이 총 수업 시간 1/4 초과일 때는 F(학점 미부여) 출력
        print("F (학점 미부여)") 
    else:
        attendance_score_formula = 20 - (20 * (ah + (tc / 3)) / (hpw * 15)) # 출석 점수 공식 작성
        print(f"당신의 점수는 {float(attendance_score_formula):.2f}점입니다.")

# 2. 출석 점수 결정에 필요한 인자값들 입력 받기
hours_per_week = int(input("일주일 수업 시간을 입력하시오: "))
absence_hours = int(input("총 결석한 시간을 입력하시오: "))
tardy_count = int(input("총 지각한 횟수를 입력하시오: "))

# 3. 출석 점수를 함수를 거쳐 돌려 받는다.
attendance_score(hours_per_week, absence_hours, tardy_count)





#____________________________________________________________

# 지각을 결석으로 계산해 줄 때 나머지를 떼는 명령어를 넣었을 때 교안의 답과 일치한다.
# def attendance_score(hpw, ah, tc):
#     if (ah + (tc // 3)) > ((hpw * 15) / 4):
#         print("F (학점 미부여)") 
#     else:
#         attendance_score_formula = 20 - (20 * (ah + (tc // 3)) / (hpw * 15))
#         print(f"당신의 점수는 {float(attendance_score_formula):.2f}점입니다.")