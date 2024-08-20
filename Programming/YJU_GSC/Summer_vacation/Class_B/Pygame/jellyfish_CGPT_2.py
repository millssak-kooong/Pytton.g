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
def score(feed_amount):
    score_font = pygame.font.SysFont('comicsansms', 30)
    value = score_font.render(f"Last egg {feed_amount}", True, (0, 0, 0))
    screen.blit(value, [0, 0])

# -------------- Feed
list_feed = []
feed_amount = random.randint(1, 100)
def feed():
    global list_feed
    list_feed = []  # Reset
    for _ in range(feed_amount):
        feed_r = random.randint(1, 10)
        feed_clr = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        feed_x = random.randint(feed_r - 1, screen_w - 1 - feed_r)
        feed_y = random.randint(feed_r - 1, screen_h - 1 - feed_r)
        list_feed.append((feed_x, feed_y, feed_clr, feed_r))

def feed_draw():
     for feed in list_feed:
        pygame.draw.circle(screen, feed[2], (feed[0], feed[1]), feed[3])

# -------------- Net
net_rect_side = 20
net_rect_clr = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
net_x, net_y = (screen_w - 1) // 2, (screen_h - 1) // 2
list_net = [(net_x, net_y)]
direction = 'right'

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
        message_rect = message.get_rect(center = ((screen_w - 1) // 2, (screen_h - 1) // 2))
        screen.blit(message, message_rect)
        pygame.display.update()
    return direction

feed()

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

    # 화면 밖에 나가지 않도록 하는 코드
    if net_x < 0 or (net_x + net_rect_side) > screen_w or net_y < 0 or (net_y + net_rect_side) > screen_h:
        running = False

    list_net.append((net_x, net_y))
    if len(list_net) > 1:
        list_net.pop(0)
    
    screen.fill(white)
    score(feed_amount)
    feed_draw()

    for net_pos in list_net:
        pygame.draw.rect(screen, net_rect_clr, [net_pos[0], net_pos[1], net_rect_side, net_rect_side])
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
