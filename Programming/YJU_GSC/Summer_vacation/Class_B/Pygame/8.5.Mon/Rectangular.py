import pygame

pygame.init() # 초기화

screen = pygame.display.set_mode((640, 480)) # 너비, 높이
pygame.display.set_caption("Rectangular Drawing")

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# 사각형 정의(사각형 객체 생성: 위치 정보 저장)
rect1 = pygame.Rect(100, 100, 100, 50)

# 게임 루프
running = True
while running: # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT이라는 이벤트를 발생시키면
            running = False # True가 False로 바뀌고 종료

    screen.fill(white) # 화면 흰색 채우기
    
    # 사각형 그리기
    pygame.draw.rect(screen, blue, rect1) # Rect 객체 이용
    pygame.draw.rect(screen, red, (200, 200, 50, 100)) # tuple 자료형 이용

    # 화면 업데이트
    pygame.display.flip()

    # clock.tick(60)

pygame.quit() # 종료