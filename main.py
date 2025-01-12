from pygame import *

'''' variables '''
bkg_color = (200,255,255)
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(bkg_color)

clock = time.Clock()


'''game loop'''
running = False
while not running:
    for e in event.get():
        if e.type == QUIT:
            running == True

    display.update()
    clock.tick(60)


