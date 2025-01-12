from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,width,height,speed):
        self.image = transform.scale(image.load(player_image), (width,height))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.x = player_y

        self.speed = speed

    def reset(self.window)
    window.blit(self.image, (self.rect.x, self.rect.x))