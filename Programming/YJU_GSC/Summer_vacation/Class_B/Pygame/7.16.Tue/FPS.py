import pygame

# 색상 정의
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init() # 파이게임 초기화
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = screen.get_width()/2
y = screen.get_height()/2
radius = 40
speed = 5

running = True
while running: # while문이 한 번 돈다는 것은 그림 한 장이고, 곧 영상이 된다.
    # 이벤트 큐에서 이벤트를 가져옴
    for event in pygame.event.get(): # 이벤트를 처리할 때는 모두 for문 안에서 처리한다.
        if event.type == pygame.QUIT:
            running = False
    # 이벤트가 발생할 때
    screen.fill((255, 255, 255)) 
    
    pygame.draw.circle(screen, RED, (x, y), radius)  
    
    if x + radius >= screen.get_width() or x - radius <= 0:
        speed = -speed
        
    x += speed

    pygame.display.flip() # 메모리에 그려서 저장해 놓은 것을 한번에 보여주는 게 flip.
    
    clock.tick(120)
    

  
# 파이게임 종료
pygame.quit()