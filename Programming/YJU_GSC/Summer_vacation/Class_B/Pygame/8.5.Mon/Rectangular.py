import pygame




# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Movement")

# 색상 정의
white = (255, 255, 255)

# 이미지 로드
# 파일 위치를 코드랑 같은 폴더 안일 때
# blue_image = pygame.image.load(r"C:\Users\USER\OneDrive - yjc.ac.kr\바탕 화면\mymy_prgrm\Programming\YJU_GSC\Summer_vacation\Class_B\Pygame\8.5.Mon\blue_rect.png")
# red_image = pygame.image.load(r"C:\Users\USER\OneDrive - yjc.ac.kr\바탕 화면\mymy_prgrm\Programming\YJU_GSC\Summer_vacation\Class_B\Pygame\8.5.Mon\red_rect.png")

# 파일 위치를 'mymy_prgrm'에 저장했을 때
blue_image = pygame.image.load("blue_rect.png")
red_image = pygame.image.load("red_rect.png")

# 이미지 초기 위치 설정
blue_rect = blue_image.get_rect()
blue_rect.topleft = (100, 100)

red_rect = red_image.get_rect()
red_rect.topleft = (200, 200)

# 이동 속도 설정
speed = 1

# 게임 루프
running = True
while running: # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT이라는 이벤트를 발생시키면
            running = False # True가 False로 바뀌고 종료

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blue_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        blue_rect.x += speed
    if keys[pygame.K_UP]:
        blue_rect.y -= speed
    if keys[pygame.K_DOWN]:
        blue_rect.y += speed
    if keys[pygame.K_a]:
        blue_rect.x -= speed
    if keys[pygame.K_d]:
        blue_rect.x += speed
    if keys[pygame.K_w]:
        blue_rect.y -= speed
    if keys[pygame.K_s]:
        blue_rect.y += speed

    # 화면 흰색 채우기
    screen.fill(white)
    
    # 이미지 그리기
    screen.blit(blue_image, blue_rect)
    screen.blit(red_image, red_rect)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()