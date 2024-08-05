def calculate_average(*args):
    return sum(args) / len(args)
print(calculate_average(1, 2, 3, 4, 5))  # 출력: 3.0
print(calculate_average(6, 7, 8))        # 출력: 7.0
print(calculate_average(10, 20))         # 출력: 15.0