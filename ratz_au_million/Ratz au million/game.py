import pygame
import math
pygame.init()
r=2

class Game:

    def __init__(self):
        self.is_playing = False
        self.vie = 3

        self.repok = False
        self.repA = 0
        self.repB = 0
        self.repC = 0
        self.repD = 0
        self.juste = 0
        self.faux = 0

        # boutton
        self.boutton = 1

        #ressource

        self.Q1RA = pygame.image.load('assets/A rep.png')
        self.Q1RA = pygame.transform.scale(self.Q1RA, (1366, 100))
        self.rectQ1RA = self.Q1RA.get_rect()
        self.rectQ1RA.x = 0
        self.rectQ1RA.y = 400

        self.Q1RB = pygame.image.load('assets/B rep.png')
        self.Q1RB = pygame.transform.scale(self.Q1RB, (1366, 100))
        self.rectQ1RB = self.Q1RB.get_rect()
        self.rectQ1RB.x = 0
        self.rectQ1RB.y = 480

        self.Q1RC = pygame.image.load('assets/C rep.png')
        self.Q1RC = pygame.transform.scale(self.Q1RC, (1366, 100))
        self.rectQ1RC = self.Q1RC.get_rect()
        self.rectQ1RC.x = 0
        self.rectQ1RC.y = 580

        self.Q1RD = pygame.image.load('assets/D rep.png')
        self.Q1RD = pygame.transform.scale(self.Q1RD, (1366, 100))
        self.rectQ1RD = self.Q1RD.get_rect()
        self.rectQ1RD.x = 0
        self.rectQ1RD.y = 678

        # juste
        self.Q1RAV = pygame.image.load('assets/A vertt.png')
        self.Q1RAV = pygame.transform.scale(self.Q1RAV, (1366, 100))
        self.rectQ1RAV = self.Q1RAV.get_rect()
        self.rectQ1RAV.x = 0
        self.rectQ1RAV.y = 400

        self.Q1RBV = pygame.image.load('assets/B vertt.png')
        self.Q1RBV = pygame.transform.scale(self.Q1RBV, (1366, 100))
        self.rectQ1RBV = self.Q1RBV.get_rect()
        self.rectQ1RBV.x = 0
        self.rectQ1RBV.y = 480

        self.Q1RCV = pygame.image.load('assets/C vertt.png')
        self.Q1RCV = pygame.transform.scale(self.Q1RCV, (1366, 100))
        self.rectQ1RCV = self.Q1RCV.get_rect()
        self.rectQ1RCV.x = 0
        self.rectQ1RCV.y = 580

        self.Q1RDV = pygame.image.load('assets/D vertt.png')
        self.Q1RDV = pygame.transform.scale(self.Q1RDV, (1366, 100))
        self.rectQ1RDV = self.Q1RDV.get_rect()
        self.rectQ1RDV.x = 0
        self.rectQ1RDV.y = 678

        # Faux
        self.Q1RAF = pygame.image.load('assets/A fauxx.png')
        self.Q1RAF = pygame.transform.scale(self.Q1RAF, (1366, 100))
        self.rectQ1RAF = self.Q1RAF.get_rect()
        self.rectQ1RAF.x = 0
        self.rectQ1RAF.y = 400

        self.Q1RBF = pygame.image.load('assets/B fauxx.png')
        self.Q1RBF = pygame.transform.scale(self.Q1RBF, (1366, 100))
        self.rectQ1RBF = self.Q1RBF.get_rect()
        self.rectQ1RBF.x = 0
        self.rectQ1RBF.y = 480

        self.Q1RCF = pygame.image.load('assets/C fauxx.png')
        self.Q1RCF = pygame.transform.scale(self.Q1RCF, (1366, 100))
        self.rectQ1RCF = self.Q1RCF.get_rect()
        self.rectQ1RCF.x = 0
        self.rectQ1RCF.y = 580

        self.Q1RDF = pygame.image.load('assets/D fauxx.png')
        self.Q1RDF = pygame.transform.scale(self.Q1RDF, (1366, 100))
        self.rectQ1RDF = self.Q1RDF.get_rect()
        self.rectQ1RDF.x = 0
        self.rectQ1RDF.y = 678


        # Fleche
        self.suivant_button = pygame.image.load('assets/Fléche.png')
        self.suivant_button = pygame.transform.scale(self.suivant_button, (149, 83))
        self.suivant_button_rect = self.suivant_button.get_rect()
        self.suivant_button_rect.x = math.ceil(20)
        self.suivant_button_rect.y = math.ceil(20)

        # plateau
        self.plateau = pygame.image.load('assets/plateau.jpg')
        self.plateau = pygame.transform.scale(self.plateau, (1366, 768))

        # Scrore
        self.score = pygame.image.load('assets/score.png')
        self.score = pygame.transform.scale(self.score, (530, 450))

        self.quitter_button = pygame.image.load('assets/boutton.png')
        self.quitter_button = pygame.transform.scale(self.quitter_button, (70, 70))
        self.quitter_button_rect = self.quitter_button.get_rect()
        self.quitter_button_rect.x = math.ceil(1300)
        self.quitter_button_rect.y = math.ceil(10)

        self.v = 0
        self.liste = ["c", "d", "b", "b", "a", "d", "c", "a", "b", "a"]


    def suivant(self):
        if self.repok:
            self.boutton +=1
        else:
            self.boutton += 0
        self.repok = False
        self.repA = 0
        self.repB = 0
        self.repC = 0
        self.repD = 0

    def boutton_suivant(self,screen):
        screen.blit(self.suivant_button, self.suivant_button_rect)

    def Q1(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('Qui est-ce qui est dangereuse d’après ses camarades de classe ?', False, (255, 255, 255))
        screen.blit(TQ1, (185, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render('Elise', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('Gaël', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('Cemile', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('Guillem', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def Q2(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('Qui est-ce qui s’est pris 6 râteaux ?', False, (255, 255, 255))
        screen.blit(TQ1, (450, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render(' Avel', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('Lyse', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('Lucas B. ', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('Maurin', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def Q3(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('Qui est-ce qui a un problème avec les courbes ?', False, (255, 255, 255))
        screen.blit(TQ1, (400, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render('Le prof de math', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('Dylan', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('Lucas L.', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('Théa', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def Q4(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('Qui est la version Wish de Cemile ?', False, (255, 255, 255))
        screen.blit(TQ1, (400, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render(' Juliette', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('Naim', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('Louis', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('Thibault', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def Q5(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('Qui détient le record de retard en math ?', False, (255, 255, 255))
        screen.blit(TQ1, (400, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render(' Florian', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('Alex', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('Charly', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('Melissa', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def Q6(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('Qui est-ce qui a une méga trottinette du turfu ?', False, (255, 255, 255))
        screen.blit(TQ1, (350, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render(' Théo', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('Johann', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('Nassim', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('Timothee', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def Q7(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('Quel est la pire insulte ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render(' 232', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('32', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('132', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('142', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def Q8(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('Qui sont les incultes ?', False, (255, 255, 255))
        screen.blit(TQ1, (500, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render(' les étudiants', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('Les professeurs', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('les parents', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('les animaux', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def Q9(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('Que se passe-t-il si l’on mange un singe mort ?', False, (255, 255, 255))
        screen.blit(TQ1, (350, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render(' On devient King Kong', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('on chope ebola', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('Je donne ma langue au singe', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('on crée covid-21', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def Q10(self, screen):
        Q1 = pygame.font.SysFont('Comic Sans MS', 35)
        TQ1 = Q1.render('C’est l’anniversaire de qui aujourd’hui ?', False, (255, 255, 255))
        screen.blit(TQ1, (350, 300))

        RA = pygame.font.SysFont('Comic Sans MS', 35)
        TRA = RA.render(' Papi', False, (255, 255, 255))
        screen.blit(TRA, (600, 420))

        RB = pygame.font.SysFont('Comic Sans MS', 35)
        TRB = RB.render('Le Pape', False, (255, 255, 255))
        screen.blit(TRB, (600, 495))

        RC = pygame.font.SysFont('Comic Sans MS', 35)
        TRC = RC.render('Romain', False, (255, 255, 255))
        screen.blit(TRC, (600, 595))

        RD = pygame.font.SysFont('Comic Sans MS', 35)
        TRD = RD.render('Joel', False, (255, 255, 255))
        screen.blit(TRD, (600, 690))

    def verif(self):
        if self.repok == True:
            if self.liste[self.v] == "a":
                self.repA = 1
            elif self.liste[self.v] == "b":
                self.repB = 1
            elif self.liste[self.v] == "c":
                self.repC = 1
            elif self.liste[self.v] == "d":
                self.repD = 1

    def reponse(self,screen):
        RD = pygame.font.SysFont('Comic Sans MS', 160)
        TRD = RD.render(str(self.juste), False, (0, 0, 0))
        screen.blit(TRD, (1150/r, 790/r))

        RD = pygame.font.SysFont('Comic Sans MS', 160)
        TRD = RD.render(str(self.faux), False, (0, 0, 0))
        screen.blit(TRD, (1150/r, 1000/r))


    def update(self, screen):

        #screen.blit(self.imageq1, self.rectq1)
        if self.repA == 0:
            screen.blit(self.Q1RA,self.rectQ1RA)
        elif self.repA == 1:
            screen.blit(self.Q1RAV,self.rectQ1RAV)
        elif self.repA == 2:
            screen.blit(self.Q1RAF,self.rectQ1RAF)

        if self.repB == 0:
            screen.blit(self.Q1RB, self.rectQ1RB)
        elif self.repB == 1:
            screen.blit(self.Q1RBV, self.rectQ1RBV)
        elif self.repB == 2:
            screen.blit(self.Q1RBF, self.rectQ1RBF)

        if self.repC == 0:
            screen.blit(self.Q1RC, self.rectQ1RC)
        elif self.repC == 1:
            screen.blit(self.Q1RCV, self.rectQ1RCV)
        elif self.repC == 2:
            screen.blit(self.Q1RCF, self.rectQ1RCF)

        if self.repD == 0:
            screen.blit(self.Q1RD, self.rectQ1RD)
        elif self.repD == 1:
            screen.blit(self.Q1RDV, self.rectQ1RDV)
        elif self.repD == 2:
            screen.blit(self.Q1RDF, self.rectQ1RDF)

        # Suivant
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
        else:
            screen.blit(self.plateau,(0,0))
            screen.blit(self.score,(930/r,500/r))
            screen.blit(self.quitter_button,self.quitter_button_rect)
            self.reponse(screen)



