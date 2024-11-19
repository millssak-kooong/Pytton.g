import pygame
import random
import csv
import re

# CSV 데이터를 로드
def load_questions_from_csv(file_path):
    questions = []
    all_kanji = set()  # 모든 한자를 저장할 집합
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "meaning" in row and "answer" in row and "characters" in row:
                kanji, hiragana = row["answer"].split(":")
                all_kanji.update(row.get("characters", "").split(","))  # 모든 한자를 집합에 추가
                questions.append({
                    "meaning": row["meaning"],
                    "kanji": kanji,  # 정답 전체 (한자 + 히라가나)
                    "hiragana": hiragana
                })
    return questions, sorted(all_kanji)  # 고유 한자 정렬 후 반환

# 파일 경로
csv_file_path = "hanja_data.csv"
questions, all_kanji = load_questions_from_csv(csv_file_path)

# 파이게임 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hanja Quiz")

# 폰트 설정
font_path = "NotoSerifCJKjp-Regular.otf"  # 일본어 스타일 폰트
font = pygame.font.Font(font_path, 40)
small_font = pygame.font.Font(font_path, 25)

# 색상 설정
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)

# 문제 로드 함수
def load_new_question(mode="all", num_questions=20):
    if mode == "test":  # 20개 테스트 모드
        selected_questions = random.sample(questions, min(num_questions, len(questions)))
    else:  # 모든 한자 외우기 모드
        selected_questions = random.sample(questions, len(questions))  # 모든 문제를 랜덤으로 정렬
    return selected_questions


# 게임 데이터 초기화 함수
def reset_game():
    global total_questions, current_question, correct_kanji, display_text, user_answer, feedback, show_feedback_timer, show_feedback, question_index, correct_count, incorrect_count, mistake_made, current_questions, incorrect_questions
    current_questions = load_new_question()  # 초기에는 전체 한자를 사용
    total_questions = len(current_questions)
    current_question, correct_kanji, display_text = load_new_question_individual(current_questions[0])
    user_answer = [""] * len(correct_kanji)  # 정답 빈칸 초기화
    feedback = ""
    show_feedback_timer = 0  # 피드백 타이머
    show_feedback = False
    question_index = 1
    correct_count = 0
    incorrect_count = 0
    mistake_made = False
    incorrect_questions = []  # 틀린 문제들 저장

# 개별 문제 로드 함수
def load_new_question_individual(question):
    kanji_only = ''.join([char for char in question["kanji"] if re.match(r'[\u4e00-\u9fff]', char)])  # 한자만 추출
    display_text = ''.join(["ㅁ" if re.match(r'[\u4e00-\u9fff]', char) else char for char in question["kanji"]])
    return question, list(kanji_only), display_text

# 초기 게임 데이터 설정
reset_game()

# 게임 상태 설정
STATE_MENU = "menu"
STATE_GAME = "game"
STATE_RESULT = "result"
state = STATE_MENU
mode = "all"  # 현재 게임 모드 (모든 한자 외우기 or 테스트)

# 한자 보기 크기
kanji_button_width, kanji_button_height = 60, 60
columns = 15
padding = 10
kanji_start_y = 100
kanji_end_y = kanji_start_y + (len(all_kanji) // columns + 1) * (kanji_button_height + padding)
answer_start_y = kanji_end_y + 50


# 게임 루프
running = True
while running:
    screen.fill(white)

    if state == STATE_MENU:
        # 메뉴 화면 출력
        title_text = font.render("쪽지시험용 한자 외우기", True, black)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))
        made_by_text = small_font.render("made by DGK", True, black)
        screen.blit(made_by_text, (screen_width // 2 - made_by_text.get_width() // 2, 180))

        # 모든 한자 외우기 버튼
        all_button_rect = pygame.Rect(screen_width // 2 - 150, 300, 300, 80)
        pygame.draw.rect(screen, gray, all_button_rect)
        all_text = small_font.render("모든 한자 외우기", True, black)
        screen.blit(all_text, (all_button_rect.x + 50, all_button_rect.y + 25))

        # 20개 테스트 버튼
        test_button_rect = pygame.Rect(screen_width // 2 - 150, 400, 300, 80)
        pygame.draw.rect(screen, gray, test_button_rect)
        test_text = small_font.render("20개 테스트", True, black)
        screen.blit(test_text, (test_button_rect.x + 70, test_button_rect.y + 25))

        # 이벤트 처리 (버튼 클릭 확인)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if all_button_rect.collidepoint(x, y):
                    # 모든 한자 외우기 모드 시작
                    mode = "all"
                    reset_game()
                    state = STATE_GAME
                elif test_button_rect.collidepoint(x, y):
                    # 20개 테스트 모드 시작
                    mode = "test"
                    current_questions = load_new_question(mode="test", num_questions=20)
                    total_questions = len(current_questions)
                    current_question, correct_kanji, display_text = load_new_question_individual(current_questions[0])
                    question_index = 1
                    incorrect_questions = []  # 틀린 문제 초기화
                    state = STATE_GAME

    elif state == STATE_GAME:
        # 뜻 출력
        meaning_text = font.render(f"뜻: {current_question['meaning']}", True, black)
        screen.blit(meaning_text, (screen_width // 2 - meaning_text.get_width() // 2, 20))

        # 문제 번호 출력
        question_counter_text = small_font.render(f"문제: {question_index} / {total_questions}", True, black)
        screen.blit(question_counter_text, (screen_width - question_counter_text.get_width() - 20, 20))

        # 홈 버튼
        home_button_rect = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, gray, home_button_rect)
        home_text = small_font.render("홈", True, black)
        screen.blit(home_text, (home_button_rect.x + 25, home_button_rect.y + 15))

        # Pass 버튼
        pass_button_rect = pygame.Rect(screen_width - 120, screen_height - 70, 100, 50)
        pygame.draw.rect(screen, gray, pass_button_rect)
        pass_text = small_font.render("Pass", True, black)
        screen.blit(pass_text, (pass_button_rect.x + 25, pass_button_rect.y + 15))

        # 보기 출력
        buttons = []
        for i, choice in enumerate(all_kanji):
            x_start = (screen_width - (columns * (kanji_button_width + padding))) // 2
            x = x_start + (i % columns) * (kanji_button_width + padding)
            y = kanji_start_y + (i // columns) * (kanji_button_height + padding)
            button_position = (x, y, kanji_button_width, kanji_button_height)
            
            # 배경 색상 선택 (정답일 경우 녹색 표시)
            background_color = green if choice in user_answer else gray

            
            # 버튼 그리기
            pygame.draw.rect(screen, background_color, button_position)
            button_text = small_font.render(choice, True, black)
            screen.blit(button_text, (x + 10, y + 10))
            
            # 버튼 데이터 저장 (위치, 문자, 상태)
            buttons.append((button_position, choice))


        # 정답 빈칸 및 히라가나 출력
        for i, char in enumerate(display_text):
            x_start = (screen_width - (len(display_text) * (kanji_button_width + padding))) // 2
            blank_position = (x_start + i * (kanji_button_width + padding), answer_start_y, kanji_button_width, kanji_button_height)
            if char == "ㅁ" and i < len(user_answer):  # 한자 빈칸
                pygame.draw.rect(screen, gray, blank_position)
                if user_answer[i]:
                    blank_text = small_font.render(user_answer[i], True, black)
                    screen.blit(blank_text, (blank_position[0] + 10, blank_position[1] + 10))
                buttons.append((blank_position, i))  # 정답 칸
            else:
                # 히라가나 출력
                blank_text = small_font.render(char, True, black)
                screen.blit(blank_text, (blank_position[0] + 10, blank_position[1] + 10))

        # 피드백 표시
        if show_feedback:
            feedback_text = small_font.render(feedback, True, green if feedback in ["정답입니다!", "Pass"] else red)
            screen.blit(feedback_text, (screen_width // 2 - feedback_text.get_width() // 2, answer_start_y + 80))
            
            if feedback in ["정답입니다!", "Pass"]:  # 정답 또는 Pass일 때
                # 히라가나와 한자를 나란히 출력
                combined_text = f"{current_question['kanji']} ({current_question['hiragana']})"
                combined_text_rendered = font.render(combined_text, True, black)
                screen.blit(combined_text_rendered, (screen_width // 2 - combined_text_rendered.get_width() // 2, answer_start_y - 50))

            # 타이머로 피드백을 사라지게 하거나 다음 문제로 전환
            if pygame.time.get_ticks() - show_feedback_timer > 3000:  # 3초 후
                if feedback in ["정답입니다!", "Pass"]:
                    question_index += 1
                    if question_index > total_questions:
                        state = STATE_RESULT
                    else:
                        current_question, correct_kanji, display_text = load_new_question_individual(
                            current_questions[question_index - 1]
                        )
                        user_answer = [""] * len(correct_kanji)
                    mistake_made = False
                else:
                    incorrect_count += 1
                    if current_question not in incorrect_questions:  # 중복 방지
                        incorrect_questions.append(current_question)
                feedback = ""
                show_feedback = False

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # 홈 버튼 클릭 확인
                if home_button_rect.collidepoint(x, y):
                    state = STATE_MENU

                # Pass 버튼 클릭 확인
                elif pass_button_rect.collidepoint(x, y):
                    feedback = "Pass"
                    show_feedback_timer = pygame.time.get_ticks()
                    show_feedback = True

                    # 정답 한자들을 user_answer에 추가하여 배경색을 녹색으로
                    for kanji in correct_kanji:
                        if kanji not in user_answer:
                            user_answer.append(kanji)  # 정답 리스트에 추가


                for button in buttons:
                    button_position, value = button
                    if (
                        button_position[0] <= x <= button_position[0] + button_position[2]
                        and button_position[1] <= y <= button_position[1] + button_position[3]
                    ):
                        if isinstance(value, int):  # 정답 칸 클릭
                            user_answer[value] = ""  # 정답 삭제
                        elif value in correct_kanji:  # 보기에서 정답 클릭
                            for i in range(len(user_answer)):
                                if not user_answer[i]:  # 첫 번째 빈칸에 넣기
                                    user_answer[i] = value
                                    break
                            # 정답 확인
                            if "".join(user_answer) == "".join(correct_kanji):  # 한자만 비교
                                feedback = "정답입니다!"
                                show_feedback_timer = pygame.time.get_ticks()
                                show_feedback = True
                        

    pygame.display.flip()

pygame.quit()
