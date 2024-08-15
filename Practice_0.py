import pygame

# Pygame 초기화
pygame.init()

# 디스플레이 정보 가져오기
info = pygame.display.Info()

# 최대 화면 크기 출력
print(f"Max Screen Width: {info.current_w}")
print(f"Max Screen Height: {info.current_h}")

# Pygame 종료
pygame.quit()