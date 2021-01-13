import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine


zone_affichage = tk.Label(racine, text="test")
zone_affichage.grid(column=2, row=0, columnspan=2)

un = tk.Button(racine, text="1", width=3, height=3)
un.grid(column=0, row=1)

deux = tk.Button(racine, text="2", width=3, height=3)
deux.grid(column=1, row=1)

trois = tk.Button(racine, text="3", width=3, height=3)
trois.grid(column=2, row=1)

quatre = tk.Button(racine, text="4", width=3, height=3)
quatre.grid(column=0, row=2)

cinq = tk.Button(racine, text="5", width=3, height=3)
cinq.grid(column=1, row=2)

six = tk.Button(racine, text="6", width=3, height=3)
six.grid(column=2, row=2)

sept = tk.Button(racine, text="7", width=3, height=3)
sept.grid(column=0, row=3)

huit = tk.Button(racine, text="8", width=3, height=3)
huit.grid(column=1, row=3)

neuf = tk.Button(racine, text="9", width=3, height=3)
neuf.grid(column=2, row=3)

zero = tk.Button(racine, text="0", width=3, height=3)
zero.grid(column=1, row=4)

plus = tk.Button(racine, text="+", width=3, height=3)
plus.grid(column=3, row=1)

moins = tk.Button(racine, text="-", width=3, height=3)
moins.grid(column=3, row=2)

fois = tk.Button(racine, text="x", width=3, height=3)
fois.grid(column=3, row=3)

diviser = tk.Button(racine, text="/", width=3, height=3)
diviser.grid(column=3, row=4)

virgule = tk.Button(racine, text=".", width=3, height=3)
virgule.grid(column=2, row=4)






racine.mainloop() # Lancement de la boucle principale
#Pour lancer une fenêtre 

