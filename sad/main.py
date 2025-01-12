from pygame import *
from spriteClass import GameSprite, Player
'''' variables '''
bkg_color = (200, 255, 255)
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(bkg_color)

clock = time.Clock()

''' objects '''
ball = GameSprite(player_image='sad/baller.jpg',
                   player_x=250, player_y=250, 
                   width=50, heigth=50, speed=2)

rocket_left = Player(player_image='sad/paddler.jpg',
                   player_x=10, player_y=220, 
                   width=50, heigth=150, speed=4)

rocket_right = Player(player_image='sad/paddler.jpg',
                   player_x=540, player_y=220, 
                   width=50, heigth=150, speed=4)

''' game loop '''
running = False
while not running:

    ball.reset(window)
    rocket_left.reset(window)
    rocket_left.update_p_left()

    rocket_right.reset(window)
    rocket_right.update_p_right()

    for e in event.get():
        if e.type == QUIT:
            running == True

    display.update()
    clock.tick(60) 
