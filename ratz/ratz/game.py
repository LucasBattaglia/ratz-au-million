import pygame
from player import Player
from fromage_event import *

pygame.init()

class Game:

    def __init__(self):
        self.is_playing = False
        self.move = False
        self.player = Player()
        self.fromage_event = FromageFallEvent(self)
        self.pressed = {}

    def update(self,screen):

        # Player
        screen.blit(self.player.image, self.player.rect)

        # Fromage
        self.fromage_event.all_fromage.draw(screen)

        # Verifier jeu ouvert
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < (1536-436):
            self.player.move_right()
            self.move = True
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
            self.move = True
        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 160:
            self.player.move_up()
            self.move = True
        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y < (864 - 405):
            self.player.move_down()
            self.move = True
