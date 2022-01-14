import pygame
import math
from game import Game


pygame.init()
pygame.mixer.init()

game_playing = False

# fenetre du jeu
pygame.display.set_caption("Ratz Game")
image = pygame.image.load('assets/icon.png')
pygame.display.set_icon(image)
a = 1536
b = 864
screen = pygame.display.set_mode((a, b), pygame.FULLSCREEN)

# arriere plan du menu
back_menu = pygame.image.load('assets/ratz2.jpg').convert(screen)
back_menu = pygame.transform.scale(back_menu, (a, b))

# arriere plan du jeu
background = pygame.image.load('assets/fondj.jpg')
background = pygame.transform.scale(background, (a, b))

game = Game()

"""
# musique
pygame.mixer.Sound("mus.mp3")
pygame.mixer.Sound.play()
"""

# Bouton Play
play_button = pygame.image.load('assets/playbut.png')
play_button = pygame.transform.scale(play_button, (250, 250))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(150)
play_button_rect.y = math.ceil(600)

# Parametre
para_button = pygame.image.load('assets/para_button.png')
para_button = pygame.transform.scale(para_button, (250, 250))
para_button_rect = play_button.get_rect()
para_button_rect.x = math.ceil(150)
para_button_rect.y = math.ceil(1100)

# Quitter
quitter_button = pygame.image.load('assets/quitter.png')
quitter_button = pygame.transform.scale(quitter_button, (125, 125))
quitter_button_rect = play_button.get_rect()
quitter_button_rect.x = math.ceil(1400)
quitter_button_rect.y = math.ceil(20)

# boucle du jeu
running = True

while running:

    if game.is_playing:
        screen.blit(background, (0, 0))
        screen.blit(quitter_button, quitter_button_rect)
        game.update(screen)
    else:
        screen.blit(back_menu, (0, 0))
        screen.blit(play_button, play_button_rect)
        screen.blit(para_button, para_button_rect)
        screen.blit(quitter_button, quitter_button_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # Pour fermer la fenetre
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.is_playing = True
            if quitter_button_rect.collidepoint(event.pos):
                running = False
                pygame.quit()
