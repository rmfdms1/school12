import pygame

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)

bomb_image = pygame.image.load('bomb.png')
bombs = []
for i in range(3):
    bomb = bomb_image.get_rect(left=(i + 1) * 100, top=(i + 1) * 100)
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

    if girl.left < 0:
        girl.left = 0
    elif girl.right > 600:
        girl.right = 600

    #그리기

    for bomb in bombs:
        screen.blit(bomb_image, bomb)

    screen.blit(girl_image, girl)

    pygame.display.update()
    clock.tick(30) #초당 프레임수

pygame.quit() 