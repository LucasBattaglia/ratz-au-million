import pygame
import random

class Fromage(pygame.sprite.Sprite):

    def __init__(self,fromage_event):
        super().__init__()
        self.image = pygame.image.load('assets/fromage.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,5)
        #self.rect.x = random.randint(2600,2700)
        #self.rect.y = random.randint(160,1600)
        self.fromage_event = fromage_event

    def removed(self):
        self.fromage_event.all_fromage.remove(self)

    def fall(self):
        self.rect.x -= self.velocity
        if self.rect.x < 10:
            print("test ok")
            #self.removed()
