import random

while True:

    # 1. 사용자 입력

    value = int(input("Enter the number of dice rolls (between 100 and 1,000,000): ")) # 사용자 입력값

    if 100 <= value <= 1000000: # 입력값 범위 설정
        
    # 2. 난수 생성 및 카운트

        # 주사위 리스트 만들기
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []

        # 입력값만큼 주사위 돌리기
        for x in range(0, value):

            # 주사위 만들기
            dice = random.randint(1, 6)
            # print(dice)

            # 주사위 리스트에 담기
            if dice == 1:
                list1.append(dice)
            elif dice == 2:
                list2.append(dice)
            elif dice == 3:
                list3.append(dice)
            elif dice == 4:
                list4.append(dice)
            elif dice == 5:
                list5.append(dice)
            else:
                list6.append(dice)
        # print(len(list1), len(list2))

        # 주사위 확률 구하기
            # 주사위 나온 횟수
        times1 = len(list1)
        times2 = len(list2)
        times3 = len(list3)
        times4 = len(list4)
        times5 = len(list5)
        times6 = len(list6)
        # print(times1, times2)
        
            # 주사위 번호당 확률
        percentage1 = times1 / value * 100
        percentage2 = times2 / value * 100
        percentage3 = times3 / value * 100
        percentage4 = times4 / value * 100
        percentage5 = times5 / value * 100
        percentage6 = times6 / value * 100
        # print(percentage1, percentage2)

# 3. 결과 시각화

        # 주사위 빈도를 별로 시각화
            # 횟수 리스트 만들기
        list_times = [times1, times2, times3, times4, times5, times6]
        # print(list_times)

            # 가장 큰 횟수 찾기
        list_max = [] # 최댓값이 여러개일 경우의 예외 처리를 위한 리스트 만들기

        for _ in list_times: # 최대값이 복수일 경우를 대비해 '이상' 연산자를 사용
            if _ >= times1 and _ >= times2 and _ >= times3 and _ >= times4 and _ >= times5 and _ >= times6:
                list_max.append(_)
        # print(list_max[0]) # 최대값이 여러개이더라도 하나만 출력

            # 별로 도식화 하기(별의 개수는 정수 자리로 판단)
        star1 = "*" * int(times1 / list_max[0] * 10)
        star2 = "*" * int(times2 / list_max[0] * 10)
        star3 = "*" * int(times3 / list_max[0] * 10)
        star4 = "*" * int(times4 / list_max[0] * 10)
        star5 = "*" * int(times5 / list_max[0] * 10)
        star6 = "*" * int(times6 / list_max[0] * 10)
        # print(star1)
        # print(times1 / list_max[0] * 10) # 주사위 1번일 때 상대적 빈도와 밑에 라인에 별 그리기
        # print(int(times1 / list_max[0] * 10) * "*") # float에서 int로 자료형 변환 후 소수점은 때고 별 그리기

            # 최종 출력 후 종료(가독성을 위해 계산할 것들은 변수로 선언해 주고 사용)
        print("Dice Roll Frequency Histogram:")
        print(f"1: {star1} ({times1} times, {percentage1}%)\n2: {star2} ({times2} times, {percentage2}%)")
        print(f"3: {star3} ({times3} times, {percentage3}%)\n4: {star4} ({times4} times, {percentage4}%)")
        print(f"5: {star5} ({times5} times, {percentage5}%)\n6: {star6} ({times6} times, {percentage6}%)")
        break

    # 범위 밖 입력값일 때 예외 처리
    else:
        print("Please enter a number within the specified range.")

# 약 2시간 반