import pygame
from Fromage import Fromage
from game import *


class FromageFallEvent:

    def __init__(self,game):
        self.percent = 0
        self.game = game
        self.all_fromage = pygame.sprite.Group()

    def fromage_fall(self):
        self.all_fromage.add(Fromage(self))

    def attempt_fall(self):
        self.fromage_fall()

