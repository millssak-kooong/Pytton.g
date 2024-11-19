import pygame
import random
import sys

# 한자 목록과 정답 데이터 초기화
unique_kanji_list = sorted(set([
    "求", "人", "職", "休", "要", "請", "救", "助", "急", "済", "記", "念", "録", "入", "表", "伝",
    "日", "暗", "号", "者", "起", "床", "世", "紀", "大", "家", "目", "型", "陸", "国", "会", "切", "量",
    "衆", "気", "使", "統", "領", "事", "丈", "根", "臣", "工", "小", "体", "巨", "偉", "犬", "猿",
    "仲", "愛", "太", "力", "협", "努", "능", "실", "圧", "暴", "学", "馬", "治", "医", "診", "僚",
    "官", "寮", "砂", "漠", "然", "募", "金", "공", "暮", "歳", "墓", "地", "規", "模", "様", "範", "義",
    "理", "講", "主", "意", "議", "論", "員", "不", "思", "礼", "儀", "式", "犠", "牲"
]))

correct_answers = {
    "구하다, 요구하다": "求",
    "구인": "求人",
    # 추가 단어...
}

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("한자 퀴즈 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 폰트 경로 (프로젝트 폴더에 있는 폰트 파일 경로를 사용)
font_path = "NotoSansCJKjp-Regular.ttf"
font = pygame.font.Font(font_path, 36)
large_font = pygame.font.Font(font_path, 48)

# 퀴즈 데이터
quiz_data = list(correct_answers.items())
random.shuffle(quiz_data)

# 문제 상태
current_question = 0
score = 0
selected_answer = ""
selected_index = -1

def draw_quiz(question, options, user_choice):
    """퀴즈 화면을 그리는 함수"""
    screen.fill(WHITE)

    # 문제 출력
    question_text = large_font.render(f"뜻: {question}", True, BLACK)
    screen.blit(question_text, (50, 50))

    # 보기 출력
    for i, option in enumerate(options):
        color = GREEN if i == user_choice else BLACK
        option_text = font.render(option, True, color)
        screen.blit(option_text, (50 + (i % 5) * 150, 150 + (i // 5) * 50))

    # 점수 출력
    score_text = font.render(f"점수: {score}", True, BLACK)
    screen.blit(score_text, (650, 50))

    pygame.display.flip()

def main():
    global current_question, score, selected_answer, selected_index

    running = True
    clock = pygame.time.Clock()

    while running:
        # 퀴즈 정보 가져오기
        if current_question >= len(quiz_data):
            print("퀴즈 완료!")
            break

        question, correct_kanji = quiz_data[current_question]
        options = random.sample(unique_kanji_list, 14) + [correct_kanji]
        random.shuffle(options)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                # 방향키로 선택 이동
                if event.key == pygame.K_RIGHT and selected_index < len(options) - 1:
                    selected_index += 1
                elif event.key == pygame.K_LEFT and selected_index > 0:
                    selected_index -= 1
                elif event.key == pygame.K_RETURN:
                    selected_answer = options[selected_index]
                    if selected_answer == correct_kanji:
                        score += 1
                        print("정답입니다!")
                    else:
                        print(f"틀렸습니다. 정답은 {correct_kanji}입니다.")
                    current_question += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, option in enumerate(options):
                    rect = pygame.Rect(50 + (i % 5) * 150, 150 + (i // 5) * 50, 100, 40)
                    if rect.collidepoint(mouse_pos):
                        selected_answer = option
                        if selected_answer == correct_kanji:
                            score += 1
                        else:
                            print(f"틀렸습니다. 정답은 {correct_kanji}입니다.")
                        current_question += 1

        # 화면 업데이트
        draw_quiz(question, options, selected_index)

        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
