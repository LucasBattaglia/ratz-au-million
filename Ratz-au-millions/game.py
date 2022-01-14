-import pygame
import math

pygame.init()
pygame.mixer.init()

class Game:

    def __init__(self):
        self.is_playing = False
        self.vie = 3

        self.repok = False
        self.repA = 0
        self.repB = 0
        self.repC = 0
        self.repD = 0

        # boutton
        self.boutton = 1

        #ressource

        self.imageq1 = pygame.image.load('assets/questionseul.png')
        self.imageq1 = pygame.transform.scale(self.imageq1, (2560, 310))
        self.rectq1 = self.imageq1.get_rect()
        self.rectq1.x = 0
        self.rectq1.y = 538

        self.Q1RA = pygame.image.load('assets/reponse.png')
        self.Q1RA = pygame.transform.scale(self.Q1RA, (2560, 210))
        self.rectQ1RA = self.Q1RA.get_rect()
        self.rectQ1RA.x = 0
        self.rectQ1RA.y = 838

        self.Q1RB = pygame.image.load('assets/reponse.png')
        self.Q1RB = pygame.transform.scale(self.Q1RB, (2560, 210))
        self.rectQ1RB = self.Q1RB.get_rect()
        self.rectQ1RB.x = 0
        self.rectQ1RB.y = 1028

        self.Q1RC = pygame.image.load('assets/reponse.png')
        self.Q1RC = pygame.transform.scale(self.Q1RC, (2560, 210))
        self.rectQ1RC = self.Q1RC.get_rect()
        self.rectQ1RC.x = 0
        self.rectQ1RC.y = 1220

        self.Q1RD = pygame.image.load('assets/reponse.png')
        self.Q1RD = pygame.transform.scale(self.Q1RD, (2560, 210))
        self.rectQ1RD = self.Q1RD.get_rect()
        self.rectQ1RD.x = 0
        self.rectQ1RD.y = 1408

        # Fleche
        self.suivant_button = pygame.image.load('assets/Fléche.png')
        self.suivant_button = pygame.transform.scale(self.suivant_button, (149, 83))
        self.suivant_button_rect = self.suivant_button.get_rect()
        self.suivant_button_rect.x = math.ceil(20)
        self.suivant_button_rect.y = math.ceil(20)

        self.v = 0
        self.liste = ["c", "d", "b", "b", "a", "d", "c", "a", "b", "a"]

    def suivant(self):
        self.boutton +=1
        self.repok = False
        self.repA = 0
        self.repB = 0
        self.repC = 0
        self.repD = 0

    def boutton_suivant(self,screen):
        screen.blit(self.suivant_button, self.suivant_button_rect)


    def Q1(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('Qui est-ce qui est dangereuse d’après ses camarades de classe ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render(' Elise', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('Gaël', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('Cemile', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('Guillem', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def Q2(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('Qui est-ce qui s’est pris 6 râteaux ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render(' Avel', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('Lyse', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('Lucas B. ', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('Maurin', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def Q3(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('Qui est-ce qui a un problème avec les courbes ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render('Le prof de math', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('Dylan', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('Lucas L.', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('Théa', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def Q4(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('Qui est la version Wish de Cemile ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render(' Juliette', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('Naim', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('Louis', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('Thibault', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def Q5(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('Qui détient le record de retard en math ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render(' Florian', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('Alex', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('Charly', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('Melissa', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def Q6(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('Qui est-ce qui a une méga trottinette du turfu ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render(' Théo', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('Johann', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('Nassim', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('Timothee', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def Q7(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('Quel est la pire insulte ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render(' 232', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('32', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('132', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('142', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def Q8(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('Qui sont les incultes ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render(' les étudiants', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('Les professeurs', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('les parents', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('les animaux', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def Q9(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('Que se passe-t-il si l’on mange un singe mort ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render(' On devient King Kong', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('on chope ebola', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('Je donne ma langue au singe', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('on crée covid-21', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def Q10(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 50)
        TQ1 = Q1.render('C’est l’anniversaire de qui aujourd’hui ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 638))

        RA = pygame.font.SysFont('Comic Sans MS', 50)
        TRA = RA.render(' Papi', False, (255, 255, 255))
        screen.blit(TRA, (1225, 882))

        RB = pygame.font.SysFont('Comic Sans MS', 50)
        TRB = RB.render('Le Pape', False, (255, 255, 255))
        screen.blit(TRB, (1225, 1089))

        RC = pygame.font.SysFont('Comic Sans MS', 50)
        TRC = RC.render('Romain', False, (255, 255, 255))
        screen.blit(TRC, (1225, 1289))

        RD = pygame.font.SysFont('Comic Sans MS', 50)
        TRD = RD.render('Joel', False, (255, 255, 255))
        screen.blit(TRD, (1225, 1489))

    def update(self, screen):
        # Q
        #screen.blit(self.imageq1, self.rectq1)
        screen.blit(self.Q1RA,self.rectQ1RA)
        screen.blit(self.Q1RB, self.rectQ1RB)
        screen.blit(self.Q1RC, self.rectQ1RC)
        screen.blit(self.Q1RD, self.rectQ1RD)

        # Suivant
        while self.repok:
            self.boutton_suivant(screen)


        # Question affichage
        if self.boutton == 1:
            self.Q1(screen)
        elif self.boutton == 2:
            self.Q2(screen)
        elif self.boutton == 3:
            self.Q3(screen)
        elif self.boutton == 4:
            self.Q4(screen)
        elif self.boutton == 5:
            self.Q5(screen)
        elif self.boutton == 6:
            self.Q6(screen)
        elif self.boutton == 7:
            self.Q7(screen)
        elif self.boutton == 8:
            self.Q8(screen)
        elif self.boutton == 9:
            self.Q9(screen)
        elif self.boutton == 10:
            self.Q10(screen)


