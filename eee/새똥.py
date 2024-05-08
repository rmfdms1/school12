import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)

large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 36)
score = 0
game_over = False

bomb_image = pygame.image.load('bomb.png')
bombs = []
for i in range(3):
    bomb = bomb_image.get_rect(left=random.randint(0, 600 - bomb.width), top=-100)
    bombs.append(bomb)

girl_image = pygame.image.load('girl.png')
girl = girl_image.get_rect(centerx=300, bottom=800)

while True:
    screen.fill((0, 0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            girl.left -= 5
        elif event.key == pygame.K_RIGHT:
            girl.left += 5

    for bomb in bombs:
        bomb.top += 5
        if bomb.top > 800:
            bombs.remove(bomb)
            bomb = bomb_image.get_rect(left=random.randint(0, 600 - bomb_image.get_width()), top=-100)
            bombs.append(bomb)
            score += 1

    if girl.left < 0:
        girl.left = 0
    elif girl.right > 600:
        girl.right = 600

    for bomb in bombs:
        if bomb.colliderect(girl):
            game_over = True

    #그리기

    for bomb in bombs:
        screen.blit(bomb_image, bomb)

    screen.blit(girl_image, girl)

    score_image = small_font.render('점수 {}'.format(score), True, (255 ,255, 0))
    screen.blit(score_image, (10, 10))

    if game_over:
        game_over_image = large_font.render('게임 종료', True, (255 ,0, 0))
        screen.blit(game_over_image, (300 - game_over_image.get_width() // 2, 400 - game_over_image.get_height() // 2))     

    pygame.display.update()
    clock.tick(30) #초당 프레임수

pygame.quit() 