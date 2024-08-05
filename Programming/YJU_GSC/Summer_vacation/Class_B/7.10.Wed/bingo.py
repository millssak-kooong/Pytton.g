# print(__name__) # Python의 Magic Validation 마법 함수
# 실행 시키면 '__main__'이 출력된다.

def print_n():
    print("kkkkk")

def print_p():
    print("ppppp")

def main():
    print_n()
    print_p()

if __name__ == "__main__":
    main()
# 현재 이곳, bingo.py 모듈 내에서만 magic validation이 '참'이다.
# 하지만 다른 파일, main.py 모듈에서 이 모듈을 불러 올 때는
# "__main__"을 "bingo"로 바꿔 주면 현재 이 모듈 내에서는 거짓이 되지만
# main.py 모듈 내에서는 참이 되어 bingo.py 모듈을 불러와서 실행할 수 있게 된다.