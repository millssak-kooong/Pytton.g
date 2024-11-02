### 지수 함수 Exponential Function ###
### 2024.10.2.수 - 과제 ###

import matplotlib.pyplot as plt

# 초기 값 설정
p_1999 = 89000 # 1999년 인구
p_2020 = 210000 # 2020년 인구
t = 2020 - 1999 # 기준년도 차이
r = (p_2020 / p_1999) ** (1 / t) - 1 # 인구 증가율 계산

# 인구 예측 함수
def predict_population(p0, r, n):
    return p0 * (1 + r) ** n

# 원하는 연도를 입력받아 인구 예측
x_year = int(input("Input the year you want to know: "))
n = x_year - 2020 # 2020년을 기준으로 n년 후

# 예측 인구 계산
predicted_population = predict_population(p_2020, r, n)

# 결과 출력
print(f"Predicted population of {x_year} is {predicted_population:.0f}.")

#------------------------------------

# 1999년부터 2100년까지의 인구 예측
years = list(range(1999, 2101))
populations = [predict_population(p_1999, r, year - 1999) for year in years]

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(years, populations, marker='o', color='b', label="Predicted Population")

# 그래프 제목 및 라벨 설정
plt.title("Predicted Population from 1999 to 2100", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Population", fontsize=14)
plt.grid(True)
plt.legend()

# 그래프 출력
plt.show()