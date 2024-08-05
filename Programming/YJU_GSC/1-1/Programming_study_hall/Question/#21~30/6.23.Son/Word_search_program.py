# 검색할 문자열을 입력하세요: test2 
# 해당 문자열이 없습니다. 다시 입력해주세요.
# 검색할 문자열을 입력하세요: pos
# 검색된 문자열의 개수: 5
# 검색된 문자열의 위치: [0, 4, 31, 39, 53]
# 단어의 개수: 13
# 전체 문자 수: 43
# 줄 수: 3
##########################################

sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

#----------------------------
# 1. 보기 중에서 문자열을 받는다.
while True:

    ### 글자 단위 리스트 만들기 ###
    list_letter = []
    list_letter += sentence # 어팬드는 사용 불가(한 문장 통째으로 들어감) list_letter.append(sentence)
    # print(list_letter)

    ### 단어 단위 리스트 만들기 ###
    list_word = sentence.split()
    # print(list_word)

    # 문자열 받기
    value = input("검색할 문자열을 입력하세요: ")

# 2. 문자열이 보기 중에 있으면 결과 출력 후 종료
    if value in list_word:
        
        # <value 수> 이런 방법도 있다(count_word = list_word.count(value))
        n_word = 0
        for a in list_word:
            if value == a:
                n_word += 1
        print(f"검색된 문자열의 개수: {n_word}")

        # <value 위치> 입력된 단어를 리스트로 만들어 첫 글자를 비교해서 그 자리 값을 알아낸다.
        list_value = [] # [p, o, s]
        list_value += value
        # print(list_value)
        location = 0
        list_location = []
        for b in list_letter:
            if list_value[0] == b:
                list_location.append(location) # 이거 "list_location += str(location)"는 안 됨: location이 int인데 str으로 바꿔더라도 십의 자리 수도 문자로 하나씩 쪼개져서 추가됨.
            location += 1
        print(f"검색된 문자열의 위치: {list_location}")

        # <단어 종류 수>
        print(f"단어의 개수: {len(list_word)}")

        # <전체 글자 수>
        n_letter = 0
        for c in list_letter:
            if c == " " or c == "\n":
                continue
            n_letter +=  1
        print(f"전체 문자 수: {n_letter}")
        
        # <행 수>
        n_row = 0
        for d in sentence:
            if d == "\n":
                n_row +=  1
        print(f"줄 수: {n_row + 1}")
        
        break

# 3. 보기에 없으면 재입력 요구
    else:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")