from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, heigth, speed):
        self.image = transform.scale(image.load(player_image) , (width, heigth))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        self.speed = speed

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update_p_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed

    def update_p_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed
