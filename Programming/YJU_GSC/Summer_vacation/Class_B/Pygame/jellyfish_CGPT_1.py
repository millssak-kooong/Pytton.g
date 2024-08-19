import random
import pygame

# -------------- Initialize
pygame.init()

# -------------- Display
screen_w = 800
screen_h = 600
screen_center = ((screen_w - 1) // 2, (screen_h - 1) // 2)
screen = pygame.display.set_mode((screen_w, screen_h))
white = (255, 255, 255)
screen.fill(white)
pygame.display.set_caption("Jellyfish")

# -------------- Speed
clock = pygame.time.Clock()
fps = 30
speed = 10

# -------------- Score
def score(score):
    score_font = pygame.font.SysFont('comicsansms', 30)
    value = score_font.render(f"Last egg {score}", True, (0, 0, 0))
    screen.blit(value, [0, 0])

# -------------- Feed
list_feed = []
feed_amount = random.randint(5, 10)  # 한번에 그려질 먹이의 개수

def generate_feed():
    global list_feed
    list_feed = []  # 초기화
    for _ in range(feed_amount):
        feed_r = random.randint(5, 10)
        feed_clr = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        feed_x = random.randint(feed_r, screen_w - feed_r)
        feed_y = random.randint(feed_r, screen_h - feed_r)
        list_feed.append((feed_x, feed_y, feed_r, feed_clr))

def draw_feed():
    for feed in list_feed:
        pygame.draw.circle(screen, feed[3], (feed[0], feed[1]), feed[2])

# -------------- Net (Snake)
net_radius = 20
net_x, net_y = screen_center
direction = 'right'
list_net = [(net_x, net_y)]

def handle(direction, net_x, net_y, speed): # Move
    if direction == 'right':
        net_x += speed
    elif direction == 'left':
        net_x -= speed
    elif direction == 'up':
        net_y -= speed
    elif direction == 'down':
        net_y += speed
    return net_x, net_y

def start_direction():
    direction = None
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    screen.fill(white)
                    play = False
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    screen.fill(white)
                    play = False
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    screen.fill(white)
                    play = False
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    screen.fill(white)
                    play = False

        # Display instruction
        screen.fill(white)
        font = pygame.font.SysFont('papyrus', 40)
        message = font.render("Press an arrow key to start", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        screen.blit(message, ((screen_w - 1) // 2 - 210, (screen_h - 1) // 2 - 40))
        pygame.display.update()
    return direction

# Generate feed once at the start
generate_feed()

# -------------- Event
direction = start_direction() # First direction to move
score(feed_amount)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
    
    net_x, net_y = handle(direction, net_x, net_y, speed)

    # 화면 밖으로 나가지 않도록 처리
    net_x = max(0, min(net_x, screen_w - net_radius))
    net_y = max(0, min(net_y, screen_h - net_radius))

    list_net.append((net_x, net_y))
    if len(list_net) > 10:  # 뱀의 길이를 10으로 설정
        list_net.pop(0)

    # 화면을 지우고 다시 그리기
    screen.fill(white)
    score(feed_amount)
    draw_feed()  # 유지된 먹이 위치를 그리기

    # 뱀 그리기
    for segment in list_net:
        pygame.draw.rect(screen, (0, 0, 0), [segment[0], segment[1], net_radius, net_radius])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
