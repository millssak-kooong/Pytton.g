import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))


# 화면 초기화
screen.fill((255, 255, 255)) # 배경을 흰색으로 설정
pygame.display.flip()

# 원 그리기
# num_circles = 

for _ in range(random.randint(5, 20)):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    location = (random.randint(0, 799), random.randint(0, 599))
    diameter = random.randint(10, 100)
    pygame.draw.circle(screen, color, location, diameter)

pygame.display.flip() # 화면 업데이트

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()