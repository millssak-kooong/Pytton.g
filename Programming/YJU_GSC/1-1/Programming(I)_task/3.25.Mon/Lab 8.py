# 영문 모음 [vowel, 母音, ünlem] 판별기
## 사용자로부터 하나의 영문자를 입력받고, 해당 문자가 모음(a, e, i, o, u) 중 하나인지 아닌지를 판별하여 결과를 출력하는 프로그램을 작성

# 1. 사용자에게 하나의 영문자를 받는다.

vowel = input("알파벳을 하나 입력해 주세요.: ")

# 2. 입력받은 하나의 영문자가 모음인지 아닌지 판별하여 출력한다.

if vowel == "A" or vowel == "a": # 알파벳 A 또는 a일 때 모음을 출력한다.
    print(vowel, "은 모음 알파벳입니다.")

elif vowel == "E" or vowel == "e": # 알파벳 E 또는 e일 때 모음을 출력한다.
    print(vowel, "은 모음 알파벳입니다.")

elif vowel == "I" or vowel == "i": # 알파벳 I 또는 i일 때 모음을 출력한다.
    print(vowel, "은 모음 알파벳입니다.")

elif vowel == "O" or vowel == "o": # 알파벳 O 또는 o일 때 모음을 출력한다.
    print(vowel, "은 모음 알파벳입니다.")

elif vowel == "U" or vowel == "u": # 알파벳 U 또는 u일 때 모음을 출력한다.
    print(vowel, "은 모음 알파벳입니다.")
    
# 3. 모음이 아닐 때 판별 결과를 출력한다.
    
else:
    print(vowel, "은 모음 알파벳이 아닙니다.")