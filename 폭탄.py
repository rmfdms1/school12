import pygame
import random

pygame.init()  # 파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 화면 크기 설정
clock = pygame.time.Clock()

# 변수
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 36)
score = 0
game_over = False
max_bomb_speed = 9
girl_speed = 10  # 캐릭터 이동 속도 증가
bomb_spawn_rate = 30  # 초기 폭탄 생성 속도
bomb_spawn_increase_rate = 2  # 폭탄 생성 속도 증가율
boss_appeared = False  # 마왕 이미지 등장 여부
bomb_spawn_timer = bomb_spawn_rate  # 폭탄 생성 타이머

# 이미지 로드 및 크기 조정
girl_image = pygame.image.load('girl.png').convert_alpha()
girl_image = pygame.transform.scale(girl_image, (int(girl_image.get_width() * 0.7), int(girl_image.get_height() * 0.7)))
girl = girl_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT)

# demon.png 로드 및 크기 조정
demon_image = pygame.image.load('demon.png').convert_alpha()
demon_image = pygame.transform.scale(demon_image, (girl.width // 2, girl.height // 2))
bombs = []

# light.png 로드 및 크기 조정
light_image = pygame.image.load('light.png').convert_alpha()
light_image = pygame.transform.scale(light_image, (girl.width // 2, girl.height // 2))
lights = []

# 마왕 이미지 로드 및 크기 조정
boss_image = pygame.image.load('boss.png').convert_alpha()
boss_image = pygame.transform.scale(boss_image, (SCREEN_WIDTH, boss_image.get_height() // 2))  # 이미지 크기 조정
boss = boss_image.get_rect(centerx=SCREEN_WIDTH // 2, top=0)  # 마왕 위치 설정

pygame.mixer.init()
pygame.mixer.music.load('music.mid')  # 배경 음악
pygame.mixer.music.play(-1)  # -1: 무한 반복, 0: 한 번
game_over_sound = pygame.mixer.Sound('game_over.wav')

def spawn_bomb():
    global bomb_spawn_rate
    bomb = demon_image.get_rect(left=random.randint(0, SCREEN_WIDTH), top=-100)
    dy = random.randint(3, max_bomb_speed)
    bombs.append((bomb, dy))

def spawn_light():
    light = light_image.get_rect(left=random.randint(0, SCREEN_WIDTH), top=-100)
    dy = random.randint(3, max_bomb_speed)
    lights.append((light, dy))

def add_bombs(num):
    for _ in range(num):
        spawn_bomb()

def add_lights(num):
    for _ in range(num):
        spawn_light()

# 초기에 폭탄 생성
add_bombs(4)
add_lights(2)

while True:  # 게임 루프
    screen.fill(BLACK)  # 단색으로 채워 화면 지우기

    # 변수 업데이트
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        girl.left -= girl_speed
    if keys[pygame.K_RIGHT]:
        girl.left += girl_speed
    if keys[pygame.K_UP]:
        girl.top -= girl_speed
    if keys[pygame.K_DOWN]:
        girl.top += girl_speed

    for event in pygame.event.get():  # 이벤트 처리
        if event.type == pygame.QUIT:
            pygame.quit()

    if not game_over:
        bomb_spawn_timer -= 1  # 폭탄 생성 타이머 감소
        if bomb_spawn_timer <= 0:
            spawn_bomb()
            spawn_light()  # light 생성
            bomb_spawn_timer = bomb_spawn_rate  # 타이머 리셋

        for bomb, dy in bombs:
            bomb.top += dy
            if bomb.top > SCREEN_HEIGHT:
                bombs.remove((bomb, dy))
                spawn_bomb()  # 새로운 폭탄 생성
                score += 1

        for light, dy in lights:
            light.top += dy
            if light.top > SCREEN_HEIGHT:
                lights.remove((light, dy))
                spawn_light()  # 새로운 light 생성
                score += 10  # light와 충돌 시 점수 10점 추가

        if girl.left < 0:
            girl.left = 0
        elif girl.right > SCREEN_WIDTH:
            girl.right = SCREEN_WIDTH
        if girl.top < 0:  # 화면 위로 벗어나지 않도록 함
            girl.top = 0
        elif girl.bottom > SCREEN_HEIGHT:  # 화면 아래로 벗어나지 않도록 함
            girl.bottom = SCREEN_HEIGHT

        for bomb, dy in bombs:
            if bomb.colliderect(girl):
                game_over = True
                pygame.mixer.music.stop()
                game_over_sound.play()

        for light, dy in lights:
            if light.colliderect(girl):
                lights.remove((light, dy))
                score += 10  # 충돌 시 점수 10점 추가

        # 점수가 150점이 넘어갈 때 마왕 등장 및 폭탄 빈도수 증가
        if score >= 150 and not boss_appeared:
            boss_appeared = True
            max_bomb_speed *= 2  # 폭탄 최대 속도 증가
            bomb_spawn_rate = 10  # 폭탄 생성 속도 설정
            add_bombs(6)  # 추가 폭탄 생성

    # 화면 그리기

    for bomb, dy in bombs:
        screen.blit(demon_image, bomb)

    for light, dy in lights:
        screen.blit(light_image, light)

    screen.blit(girl_image, girl)

    score_image = small_font.render('점수 {}'.format(score), True, YELLOW)
    screen.blit(score_image, (10, 10))

    if boss_appeared:
        screen.blit(boss_image, boss)  # 마왕 이미지 그리기

    if game_over:
        game_over_image = large_font.render('게임 종료', True, RED)
        screen.blit(game_over_image, game_over_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    pygame.display.update()  # 모든 화면 그리기 업데이트
    clock.tick(30)  # 30 FPS (초당 프레임 수) 를 위한 딜레이 추가