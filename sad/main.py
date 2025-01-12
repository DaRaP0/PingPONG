from pygame import *
from spriteClass import GameSprite
'''' variables '''
bkg_color = (200,255,255)
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(bkg_color)

clock = time.Clock()

'''objects'''
ball = GameSprite(player_image='sad/baller.jpg'
                    player_x = 250,
                    player_y = 250,
                    width = 30,
                    height = 50,
                    speed = 2)

racket = GameSprite(player_image='sad/paddler.jpg'
                    player_x = 250,
                    player_y = 250,
                    width = 30,
                    height = 50,
                    speed = 2)


'''game loop'''
running = False
while not running:
    for e in event.get():
        if e.type == QUIT:
            running == True

    display.update()
    clock.tick(60)
