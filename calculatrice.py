import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine

racine.configure(bg="black")

nb1 = ""
nb2 = ""
type_calcul = ""


#Fonctions


def assemble_chiffres(nb):
    global nb1, nb2, type_calcul
    if type_calcul == "":
        nb1 += nb
        zone_affichage.configure(text=nb1)
    if type_calcul != "":
        nb2 += nb
        zone_affichage.configure(text=nb2)


def zeros(event=None):
    zone_affichage.configure(text="0")
    assemble_chiffres("0")


def uns(event=None):
    zone_affichage.configure(text="1")
    assemble_chiffres("1")


def deuxs(event=None):
    zone_affichage.configure(text="2")
    assemble_chiffres("2")

def troiss(event=None):
    zone_affichage.configure(text="3")
    assemble_chiffres("3")


def quatres(event=None):
    zone_affichage.configure(text="4")
    assemble_chiffres("4")

def cinqs(event=None):
    zone_affichage.configure(text="5")
    assemble_chiffres("5")


def sixs(event=None):
    zone_affichage.configure(text="6")
    assemble_chiffres("6")


def septs(event=None):
    zone_affichage.configure(text="7")
    assemble_chiffres("7")


def huits(event=None):
    zone_affichage.configure(text= "8")
    assemble_chiffres("8")


def neufs(event=None):
    zone_affichage.configure(text = "9")
    assemble_chiffres("9")


def pluss(event=None):
    global type_calcul
    zone_affichage.configure(text = "+")
    type_calcul=1


def moinss(event=None):
    global type_calcul
    zone_affichage.configure(text = "-")
    type_calcul=2


def foiss(event=None):
    global type_calcul
    zone_affichage.configure(text = "x")
    type_calcul=3


def divisers(event=None):
    global type_calcul
    zone_affichage.configure(text = "/")
    type_calcul=4


def virgules(event=None):
    zone_affichage.configure(text = ".")
    assemble_chiffres(".")

def egals(event=None):
    global type_calcul, nb1, nb2


    if type_calcul == 1:
        total = float(nb1) + float(nb2)
    elif type_calcul == 2:
        total = float(nb1) - float(nb2)
    elif type_calcul == 3:
        total = float(nb1) * float(nb2)
    elif type_calcul == 4:
        total = float(nb1) / float(nb2)
    
    zone_affichage.configure(text=total)

    nb1 = ""
    nb2 = ""
    type_calcul = ""



#Affichage

zone_affichage = tk.Label(racine, text="", bg="black", fg="white", width=20, height=5)
zone_affichage.grid(column=0, row=0, columnspan=4)

un = tk.Button(racine, text="1", width=5, height=5, bg="black", fg="white", command=uns)
un.grid(column=0, row=1)

deux = tk.Button(racine, text="2", width=5, height=5, bg="black", fg="white", command=deuxs)
deux.grid(column=1, row=1)

trois = tk.Button(racine, text="3", width=5, height=5, bg="black", fg="white", command=troiss)
trois.grid(column=2, row=1)

quatre = tk.Button(racine, text="4", width=5, height=5, bg="black", fg="white", command=quatres)
quatre.grid(column=0, row=2)

cinq = tk.Button(racine, text="5", width=5, height=5, bg="black", fg="white", command=cinqs)
cinq.grid(column=1, row=2)

six = tk.Button(racine, text="6", width=5, height=5, bg="black", fg="white", command=sixs)
six.grid(column=2, row=2)

sept = tk.Button(racine, text="7", width=5, height=5, bg="black", fg="white", command=septs)
sept.grid(column=0, row=3)

huit = tk.Button(racine, text="8", width=5, height=5, bg="black", fg="white", command=huits)
huit.grid(column=1, row=3)

neuf = tk.Button(racine, text="9", width=5, height=5, bg="black", fg="white", command=neufs)
neuf.grid(column=2, row=3)

zero = tk.Button(racine, text="0", width=5, height=5, bg="black", fg="white", command=zeros)
zero.grid(column=1, row=4)

plus = tk.Button(racine, text="+", width=5, height=5, bg="black", fg="white", command=pluss)
plus.grid(column=3, row=1)

moins = tk.Button(racine, text="-", width=5, height=5, bg="black", fg="white", command=moinss)
moins.grid(column=3, row=2)

fois = tk.Button(racine, text="x", width=5, height=5, bg="black", fg="white", command=foiss)
fois.grid(column=3, row=3)

diviser = tk.Button(racine, text="/", width=5, height=5, bg="black", fg="white", command=divisers)
diviser.grid(column=3, row=4)

virgule = tk.Button(racine, text=".", width=5, height=5, bg="black", fg="white", command=virgules)
virgule.grid(column=2, row=4)

egal = tk.Button(racine, text="=", width=5, height=5, bg="black", fg="white", command=egals)
egal.grid(column=0, row=4)


#Bind
racine.bind("<KeyPress-1>", uns)
racine.bind("<KeyPress-2>", deuxs)
racine.bind("<KeyPress-3>", troiss)
racine.bind("<KeyPress-4>", quatres)
racine.bind("<KeyPress-5>", cinqs)
racine.bind("<KeyPress-6>", sixs)
racine.bind("<KeyPress-7>", septs)
racine.bind("<KeyPress-8>", huits)
racine.bind("<KeyPress-9>", neufs)
racine.bind("<KeyPress-0>", zeros)
racine.bind("<KeyPress-+>", pluss)
racine.bind("<KeyPress-_>", moinss)
racine.bind("<KeyPress-x>", foiss)
racine.bind("<KeyPress-/>", divisers)
racine.bind("<Return>", egals)



racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 

