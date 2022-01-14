import pygame
import math
from game import *
#from moviepy.editor import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

game_playing = False

# fenetre du jeu
pygame.display.set_caption("Ratz au Milions")
a = 2560
b = 1600
screen = pygame.display.set_mode((a,b),pygame.FULLSCREEN)

# arriere plan du menu
back_menu = pygame.image.load('assets/Fond 1.jpg').convert()
back_menu = pygame.transform.scale(back_menu,(a,b))
#back_menu_rect = back_menu.get_rect()
#back_menu_rect.x = math.ceil(150)
#back_menu_rect.y = math.ceil(800)

# arriere plan du jeu
background = pygame.image.load('assets/question fond.png')
background = pygame.transform.scale(background, (a, b))

game = Game()

# musique
#son = pygame.mixer.Sound('assets/mus.mp3')
#canal = son.play()

#vidéo
#clip = VideoFileClip('Pictures/intro.mpg')

# Bouton Play
play_button = pygame.image.load('assets/play.png')
x = 554
y = 103
play_button = pygame.transform.scale(play_button, (x, y))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(a/2-(x/2))
play_button_rect.y = math.ceil(b/2-(y/2))

# Quitter
quitter_button = pygame.image.load('assets/boutton.png')
quitter_button = pygame.transform.scale(quitter_button, (125, 125))
quitter_button_rect = quitter_button.get_rect()
quitter_button_rect.x = math.ceil(2410)
quitter_button_rect.y = math.ceil(20)


# boucle du jeu
running = True

while running:

    if game.is_playing:
        screen.blit(background, (0, 0))
        screen.blit(quitter_button, quitter_button_rect)
        game.update(screen)
    else:
        screen.blit(back_menu, (0,0))
        screen.blit(play_button,play_button_rect)
        screen.blit(quitter_button, quitter_button_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # Pour fermer la fenetre
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if play_button_rect.collidepoint(event.pos):
                game.is_playing = True

            if game.suivant_button_rect.collidepoint(event.pos):
                game.boutton +=1

            if quitter_button_rect.collidepoint(event.pos):
                running = False
                pygame.quit()

            if game.rectQ1RA.collidepoint(event.pos):

                if game.liste[game.v] == "a":
                    game.repA = 1
                else:
                    game.repA = 2
                game.repok = True
                game.v +=1

            if game.rectQ1RB.collidepoint(event.pos):
                if game.liste[game.v] == "b":
                    game.repA = 1
                else:
                    game.repA = 2
                game.repok = True
                game.v += 1

            if game.rectQ1RC.collidepoint(event.pos):
                if game.liste[game.v] == "c":
                    game.repA = 1
                else:
                    game.repA = 2
                game.repok = True
                game.v += 1

            if game.rectQ1RD.collidepoint(event.pos):
                if game.liste[game.v] == "d":
                    game.repA = 1
                else:
                    game.repA = 2
                game.repok = True
                game.v += 1

