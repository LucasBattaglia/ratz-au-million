import pygame
from game import *
import vlc
from pygame.locals import *

pygame.init()
pygame.mixer.init()

game_playing = False

# fenetre du jeu
pygame.display.set_caption("Ratz au Milions")
a = 1366
b = 768
screen = pygame.display.set_mode((a,b),pygame.FULLSCREEN)

# arriere plan du menu
back_menu = pygame.image.load('assets/Fond 1.jpg').convert()
back_menu = pygame.transform.scale(back_menu,(a,b))

# arriere plan du jeu
background = pygame.image.load('assets/question fond.png')
background = pygame.transform.scale(background, (a, b))

son =pygame.mixer.Sound('assets/music_suspens2.mp3')
son.play(-1)
sound_file = vlc.MediaPlayer("C:/Users/lucas/OneDrive/Bureau/ratz_au_million/Ratz_au_million/assets/music_suspens2.mp3")
sound_file.play()

game = Game()


# Bouton Play
play_button = pygame.image.load('assets/play.png')
x = 350
y = 50
play_button = pygame.transform.scale(play_button, (x, y))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(a/2-(x/2))
play_button_rect.y = math.ceil((b/4-(y/2)))

# Quitter
quitter_button = pygame.image.load('assets/boutton.png')
quitter_button = pygame.transform.scale(quitter_button, (70, 70))
quitter_button_rect = quitter_button.get_rect()
quitter_button_rect.x = math.ceil(1300)
quitter_button_rect.y = math.ceil(10)

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
                game.suivant()

            if quitter_button_rect.collidepoint(event.pos):
                running = False
                pygame.quit()

            if game.is_playing:
                if game.rectQ1RA.collidepoint(event.pos):
                    if game.repok == False:
                        if game.liste[game.v] == "a":
                            game.repA = 1
                            game.juste += 1
                        else:
                            game.repA = 2
                            game.faux += 1
                        game.repok = True
                        game.verif()
                        game.v +=1

                if game.rectQ1RB.collidepoint(event.pos):
                    if game.repok == False:
                        if game.liste[game.v] == "b":
                            game.repB = 1
                            game.juste += 1
                        else:
                            game.repB = 2
                            game.faux += 1
                        game.repok = True
                        game.verif()
                        game.v += 1

                if game.rectQ1RC.collidepoint(event.pos):
                    if game.repok == False:
                        if game.liste[game.v] == "c":
                            game.repC = 1
                            game.juste += 1
                        else:
                            game.repC = 2
                            game.faux += 1
                        game.repok = True
                        game.verif()
                        game.v += 1


                if game.rectQ1RD.collidepoint(event.pos):
                    if game.repok == False:
                        if game.liste[game.v] == "d":
                            game.repD = 1
                            game.juste +=1
                        else:
                            game.repD = 2
                            game.faux += 1
                        game.repok = True
                        game.verif()
                        game.v += 1

