import pygame

## <<--- 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))

## <<-- fps 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
fps = 1
count = 0
## -->>

## <<--- 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    ## <<-- pygame fps 설정
    print(count)
    count += 1
    clock.tick(fps)
    ## -->>
## -->> 이미지 생성

## 게임 종료
pygame.quit()