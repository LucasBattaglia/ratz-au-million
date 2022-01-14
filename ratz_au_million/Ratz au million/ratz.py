import tkinter as tk
import tkinter.messagebox as tkm
import turtle as t


# photo1 = tk.PhotoImage(file='assets/razmo peur.png')

def droite():
    liste.append("d")


def gauche():
    liste.append("g")


def avancer():
    liste.append("a")


def reculer():
    liste.append("r")


def continuer():
    fenetre.destroy()
    a = 0
    t.width(2)
    t.speed('fastest')
    while a != len(liste):
        if liste[a] == "d":
            t.right(5)
        elif liste[a] == "d":
            t.left(5)
        elif liste[a] == "a":
            t.forward(5)
        elif liste[a] == "r":
            t.forward(-5)
        a += 1


def fermer():
    def Verification():
        mot_de_passe = "0000"
        if Motdepasse.get() == mot_de_passe:
            # le mot de passe est bon : on affiche une boîte de dialogue puis on ferme la fenêtre
            tkm.showinfo('Résultat', 'Mot de passe correct.\nAu revoir !')
            Mafenetre.destroy()
            global fenetre
            fenetre.destroy()
        else:
            # le mot de passe est incorrect : on affiche une boîte de dialogue
            tkm.showwarning('Résultat', 'Mot de passe incorrect.\nVeuillez recommencer !')
            Mafenetre.destroy()

    # Création de la fenêtre principale (main window)
    Mafenetre = tk.Toplevel()
    Mafenetre.title('Identification requise')

    # Création d'un widget Label (texte 'Mot de passe')
    Label1 = tk.Label(Mafenetre, text='Mot de passe ')
    Label1.pack(side=tk.LEFT, padx=5, pady=5)

    # Création d'un widget Entry (champ de saisie)
    Motdepasse = tk.StringVar()
    Champ = tk.Entry(Mafenetre, textvariable=Motdepasse, show='*', bg='bisque', fg='maroon')
    Champ.focus_set()
    Champ.pack(side=tk.LEFT, padx=5, pady=5)

    # Création d'un widget Button (bouton Valider)
    Bouton = tk.Button(Mafenetre, text='Valider', command=Verification)
    Bouton.pack(side=tk.LEFT, padx=5, pady=5)


fenetre = tk.Tk()
fenetre.config(background="yellow")
fenetre.attributes("-fullscreen", True)

fenetre.update()
x, y = fenetre.winfo_width(), fenetre.winfo_screenheight()

print(x, y)
# creation d'une barre de menu
menu_bar = tk.Menu(fenetre)
quit_menu = tk.Menu(menu_bar, tearoff=0)
quit_menu.add_command(label="Quitter", command=fermer)
menu_bar.add_cascade(label="Quitter", menu=quit_menu)
fenetre.config(menu=menu_bar)

liste = []

droite = tk.Button(fenetre, text="tourner a droite de 5°", font=("Corrier", 20), bg="white", fg="black", command=droite)
gauche = tk.Button(fenetre, text="tourner a gauche de 5°", font=("Corrier", 20), bg="white", fg="black", command=gauche)
avancer = tk.Button(fenetre, text="avancer de 5 pixel", font=("Corrier", 20), bg="white", fg="black", command=avancer)
reculer = tk.Button(fenetre, text="reculer de 5 pixel", font=("Corrier", 20), bg="white", fg="black", command=reculer)
continuer = tk.Button(fenetre, text="continuer", font=("Corrier", 20), bg="white", fg="black", command=continuer)

droite.place(x=x / 2, y=50)
gauche.place(x=x / 2 , y=150)
avancer.place(x=x / 2 , y=250)
reculer.place(x=x / 2 , y=350)
continuer.place(x=x / 2 , y=600)
"""
# Création d'un widget Canvas (zone graphique)
Largeur = 518
Hauteur = 807
Canevas = tk.Canvas(fenetre, width=Largeur, height=Hauteur, bg="Yellow")
item = Canevas.create_image(0, 0, anchor=tk.NW, image=photo1)
Canevas.place(x=600, y= 200)"""

# ajouter un texte
texteouv = tk.Label(fenetre, text="""Razmo aimerais dessiner mais il ne sais pas faire,
Aide le!!!
Ah non, il te cache la vue en esperant que tu ne le ridiculise pas.
Sera tu dessiner un joli dessin?
A toi de jouer""", font=("Ink Free", 20), bg="Yellow", fg="black")
texteouv.place(x=50, y=500)
fenetre.mainloop()
