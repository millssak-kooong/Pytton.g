# color = input("put the color: ")
# car = ""

# if color == "red":
#     car = "ford"
# elif color == "gray":
#     car = "bently"
# elif color == "black":
#     car = "hyundai"
# print(car)
# # line 12~19는 내가 지금까지 하던 초짜식 방법
# input_color = input("put the color: ")
# color = "red" or "gray" or "black"
# if color == "red":
#     print("ford")
# elif color == "gray":
#     print("bently")
# else:
#     print("hyundai")

# ###########################################
# # 빨간색, 검정색이 아니면 벤틀리 출력
# color = input("put the color: ")
# car = ""

# if color == "red":
#     car = "ford"
# elif color == "black":
#     car = "hyundai"
# else:
#     car = "bently"
# print(car)
# ###########################################
# color = input("put the color: ")
# car = ""

# if color == "red":
#     car = "ford"
# elif color == "gray":
#     car = "bently"
# elif color == "black" or "blue":
#     car = "hyundai"
# print(car)
###########################################

# model = input("자동차 모델을 입력 하세요: ")
# maker = ""

# if model == "M3" or "M5" or "M7":
#     maker = "BMW"
# elif model == "Y" or "X":
#     maker = "Tesla"
# elif model == "ES" or "LS":
#     maker = "Lexus"
# elif model == "G80" or "G90":
#     maker = "Hyundai"
# else:
#     maker = "알 수 없는 모델입니다."

# print(maker)
###########################################
# if 문에 in을 사용하지 말 것
# list_bmw = ["M3", "M5", "M7"]
# list_tesla = ["Y", "X"]
# list_lexus = ["ES", "LS"]
# list_hyundai = ["G80", "G90"]

# maker = "알 수 없는 모델입니다."
# model = input("자동차 모델을 입력 하세요: ")

# for i in list_bmw:
#     if i == model:
#         maker = "BMW"
# for i in list_tesla:
#     if i == model:
#         maker = "tesla"
# for i in list_lexus:
#     if i == model:
#         maker = "lexus"
# for i in list_hyundai:
#     if i == model:
#         maker = "hyundai"

# print(maker)
# #________________교수님 코드
# model = input("자동차 모델을 입력 하세요: ")

# # M1, M2, M4, M6, M8, M9, M3, M5, M7    -> BMW, 
# # Y, X          -> Tesla, 
# # ES, LS        -> Lexus
# # G80, G90      -> Hyundai
# # 이외 모델      -> "알수 없는 모델입니다."
# list_bmw = ["M1", "M2", "M4", "M6", "M8", "M9", "M3", "M5", "M7"]
# list_tesla = ["Y", "X"]
# list_lexus = ["ES", "LS"]
# list_genesis = ["G80", "G90"]

# maker = ""

# # bmw
# for model_in_list in list_bmw:
#     if model == model_in_list:
#         maker = "bmw"
#         break
        
# # tesla
# if maker == "":
#     for model_in_list in list_tesla:
#         if model == model_in_list:
#             maker = "tesla"
#             break
    
# # lexus
# if maker == "":
#     for model_in_list in list_lexus:
#         if model == model_in_list:
#             maker = "lexus"
#             break
    
# # genesis
# if maker == "":
#     for model_in_list in list_genesis:
#         if model == model_in_list:
#             maker = "genesis"
#             break

# # maker = maker if maker != "" else "알수 없는 모델입니다."

# # if model in list_bmw:
# #     maker = "bmw"
# # elif model in list_tesla:
# #     maker = "tesla"
# # elif model in list_lexus:
# #     maker = "lexus"
# # elif model in list_genesis:
# #     maker = "genesis"
# # else:
# #     make = "Unkown model"

# print(maker)

##########################################

# test = ["a", "b", "c", "d"]

# print("a" in test) # True
# print("b" in test) # True
# print("c" in test) # True
# print("d" in test) # True
# print("e" in test) # False

##########################################
# if 문에 in을 사용하지 말 것
model = input("자동차 모델을 입력 하세요: ")
list_bmw = ["M3", "M5", "M7"]
list_tesla = ["Y", "X"]
list_lexus = ["ES", "LS"]
list_hyundai = ["G80", "G90"]
# 이 외에 알 수 없는 모델 출력
list_model = [list_bmw, list_tesla, list_lexus, list_hyundai]
# 회사 목록을 가지고 온다. 반복 -> 4회 -> bmw, tesla, lexus, hyundai
##### 세로 반복 ! #####
maker_name_list = ["bmw", "tesla", "lexus", "hyundai"]
index_count = 0

for maker_list in list_model:
    # 회사별 자동차 모델을 가지고 온다 -> 반복 횟수? 회사 별 모델 개수에 따라 다름.
    ### 가로 반복 ###
    for model_in_list in maker_list:
        if model == model_in_list:
            maker = maker_name_list[index_count]
            break
        index_count += 1
        # ???미완성???

maker = ""