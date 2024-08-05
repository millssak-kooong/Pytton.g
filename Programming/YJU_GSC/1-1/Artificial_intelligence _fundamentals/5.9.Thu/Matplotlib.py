# 필요한 라이브러리를 임포트합니다.
import matplotlib.pyplot as plt # Matplotlib 그래프 사용!
import random

####### 임의 입력 데이터 생성 ###################################
#  - x축 데이터 : 1부터 99까지의 정수를 요소로 가지는 리스트 생성
x = [x_value for x_value in range(1, 100)]
#  - y축 데이터 : 1부터 100 사이의 난수를 99개 생성하여 리스트에 저장
y = [random.randint(1, 100) for y_value in range(1, 100)]
###############################################################


# Matplotlib에서 한글 폰트를 사용하기 위한 설정
plt.rc('font', family = 'Malgun Gothic')


# 1) 그래프 선택 및 데이터 입력
#  - x, y 2차원 축을 가지는 데이터를 입력
#  - .plot()는 직선 그래프를 의미
plt.plot(x, y)


# 2) 그래프 설정
 #  - 그래프의 제목을 설정
plt.title('기본 선형 그래프')

 #  - x 축 레이블을 설정
plt.xlabel('X 축')

 #  - y 축 레이블을 설정
plt.ylabel('Y 축')


# 3) 그래프를 화면에 표시
plt.show()


# 선형 그래프를 그리되, 세부 스타일 설정
# color:
#  - 선의 색상을 지정, 'red'는 선의 색상이 빨간색임을 나타냄
# linestyle:
#  - 선의 스타일을 지정'--' 점선(dashed line) 스타일을 의미
#  - 다른 옵션으로는 '-' (실선), ':' (점선), '-.' (일쇄점선) 등이 있음
# linewidth:
#  - 선의 두께를 지정
#  - 여기서 2는 선의 두께가 2 포인트(point)임을 나타냄
plt.plot(x, y, color = 'red', linestyle = '--', linewidth = 2)
# 그래프의 제목을 설정

plt.title('세부 설정된 그래프')
# X 축 레이블을 설정
plt.xlabel('X 축')
# X 축 레이블을 설정
plt.ylabel('Y 축')

# 그리드를 표시
plt.grid(True)

# 그래프를 화면에 표시
plt.show()