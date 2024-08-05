import pygame

pygame.init() # 초기화

screen = pygame.display.set_mode((640, 480)) # 너비, 높이
clock = pygame.time.Clock()
running = True

while running: # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT이라는 이벤트를 발생시키면
            running = False # True가 False로 바뀌고 종료

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit() # 종료