import pygame
import game
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 3
        self.velocity = 5
        self.image = pygame.image.load('assets/ratzmobile.png')
        self.image = pygame.transform.scale(self.image, (436, 205))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 300

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

