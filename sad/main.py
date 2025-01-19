from pygame import *
from spriteClass import GameSprite, Player
'''' variables '''
bkg_color = (200, 255, 255)
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))

clock = time.Clock()

font.init()
template = font.Font(None, 50)
lose1 = template.render('Player1 Lose!', 1, (255, 10, 50))
lose2 = template.render('Player2 Lose!', 1, (255, 10, 50))

''' objects '''
ball = GameSprite(player_image='sad/baller.jpg',
                   player_x=250, player_y=250, 
                   width=50, heigth=50, speed=2)

rocket_left = Player(player_image='sad/paddler.jpg',
                   player_x=10, player_y=220, 
                   width=20, heigth=100, speed=4)

rocket_right = Player(player_image='sad/paddler.jpg',
                   player_x=540, player_y=220, 
                   width=20, heigth=100, speed=4)

''' game loop '''
speed_x = 3
speed_y = 3



running = True
finish = False
while running:
    if not finish:
        window.fill(bkg_color)
        ball.reset(window)
        rocket_left.reset(window)
        rocket_left.update_p_left()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball, rocket_right) or sprite.collide_rect(ball, rocket_left):
            speed_x *= -1

        if ball.rect.x < 0:
            window.blit(lose1, (200, 250))
            finish = True

        if ball.rect.x > win_width:
            window.blit(lose2, (200, 250))

    rocket_right.reset(window)
    rocket_right.update_p_right()

    for e in event.get():
        if e.type == QUIT:
            running = False

    display.update()
    clock.tick(60) 
