import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine

racine.configure(bg="black")

nb1 = ""
nb2 = ""
type_calcul = ""

#Fonctions

def nombre(nb):
    global nb1, nb2

    if nb1 == "":
        nb1 = nb
    else:
        nb2 = nb



def zero():
    zone_affichage.configure(text="0")
    nombre(0)


def un():
    zone_affichage.configure(text="1")
    nombre(1)

def deux():
    zone_affichage.configure(text="2")
    nombre(2)


def trois():
    zone_affichage.configure(text="3")
    nombre(3)


def quatre():
    zone_affichage.configure(text="4")
    nombre(4)


def cinq():
    zone_affichage.configure(text="5")
    nombre(5)


def six():
    zone_affichage.configure(text="6")
    nombre(6)


def sept():
    zone_affichage.configure(text="7")
    nombre(7)


def huit():
    zone_affichage.configure(text= "8")
    nombre(8)


def neuf():
    zone_affichage.configure(text = "9")
    nombre(8)


def plus():
    global type_calcul
    zone_affichage.configure(text = "+")
    type_calcul=1


def moins():
    global type_calcul
    zone_affichage.configure(text = "-")
    type_calcul=2


def fois():
    global type_calcul
    zone_affichage.configure(text = "x")
    type_calcul=3


def diviser():
    global type_calcul
    zone_affichage.configure(text = "/")
    type_calcul=4


def virgule():
    zone_affichage.configure(text = ".")

def egal():
    global type_calcul
    
    float(nb1)
    float(nb2)
    
    if type_calcul == 1:
        total = nb1 + nb2
    elif type_calcul == 2:
        total = nb1 - nb2
    elif type_calcul == 3:
        total = nb1 * nb2
    elif type_calcul == 4:
        total = nb1 / nb2
    
    zone_affichage.configure(text=total)


#Affichage

zone_affichage = tk.Label(racine, text="test", bg="black", fg="white", width=5, height=5)
zone_affichage.grid(column=2, row=0, columnspan=2)

un = tk.Button(racine, text="1", width=5, height=5, bg="black", fg="white", command=un)
un.grid(column=0, row=1)

deux = tk.Button(racine, text="2", width=5, height=5, bg="black", fg="white", command=deux)
deux.grid(column=1, row=1)

trois = tk.Button(racine, text="3", width=5, height=5, bg="black", fg="white", command=trois)
trois.grid(column=2, row=1)

quatre = tk.Button(racine, text="4", width=5, height=5, bg="black", fg="white", command=quatre)
quatre.grid(column=0, row=2)

cinq = tk.Button(racine, text="5", width=5, height=5, bg="black", fg="white", command=cinq)
cinq.grid(column=1, row=2)

six = tk.Button(racine, text="6", width=5, height=5, bg="black", fg="white", command=six)
six.grid(column=2, row=2)

sept = tk.Button(racine, text="7", width=5, height=5, bg="black", fg="white", command=sept)
sept.grid(column=0, row=3)

huit = tk.Button(racine, text="8", width=5, height=5, bg="black", fg="white", command=huit)
huit.grid(column=1, row=3)

neuf = tk.Button(racine, text="9", width=5, height=5, bg="black", fg="white", command=neuf)
neuf.grid(column=2, row=3)

zero = tk.Button(racine, text="0", width=5, height=5, bg="black", fg="white", command=zero)
zero.grid(column=1, row=4)

plus = tk.Button(racine, text="+", width=5, height=5, bg="black", fg="white", command=plus)
plus.grid(column=3, row=1)

moins = tk.Button(racine, text="-", width=5, height=5, bg="black", fg="white", command=moins)
moins.grid(column=3, row=2)

fois = tk.Button(racine, text="x", width=5, height=5, bg="black", fg="white", command=fois)
fois.grid(column=3, row=3)

diviser = tk.Button(racine, text="/", width=5, height=5, bg="black", fg="white", command=diviser)
diviser.grid(column=3, row=4)

virgule = tk.Button(racine, text=".", width=5, height=5, bg="black", fg="white", command=virgule)
virgule.grid(column=2, row=4)

egal = tk.Button(racine, text="=", width=5, height=5, bg="black", fg="white", command=egal)
egal.grid(column=0, row=4)





racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 

