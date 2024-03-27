import pygame
#1.게임초기화
pygame.init()
#2.게임창 옵션 설정
size=[500,900]
screen=pygame.display.set_mode(size)
title='HANGMAN'
pygame.display.set_caption(title)
#3.게임내 필요한 설정
clock=pygame.time.Clock()
black=(0,0,0)
white=(255,255,255)
exit=False
#4.메인이벤트
while not exit:
#4-1.fps설정
    clock.tick(60)
#4-2.각종 입력 감지
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
#4-3.입력시간에 따른 변화
#4-4.그리기
        screen.fill(white)
#4-5. 업데이트
        pygame.display.flip()
#5.게임종료
pygame.QUIT()