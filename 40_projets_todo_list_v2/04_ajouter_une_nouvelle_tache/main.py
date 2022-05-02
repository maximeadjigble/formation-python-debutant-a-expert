from glob import glob
import tkinter as tk
from tkinter.font import Font
from taches import Taches

taches = Taches()
taches.db_connecter()
# taches.afficher()

fenetre = tk.Tk()
fenetre.title("Gestionnaire de taches")
taches_labels = []

def supprimer_labels():
    global taches_labels
    for label in taches_labels:
        label.destroy()
    taches_labels = []

def afficher_labels():
    global taches_labels
    supprimer_labels()
    for idx, tache, etat in taches.recuperer():
        # print(tache, etat)
        label = tk.Label(text=tache,
            bg='#D1E7DD' if etat else fenetre.cget('bg'),
            font=Font(family="Helvetica", size=16),
            borderwidth=1, relief="raised")
        taches_labels.append(label)
        label.pack(fill=tk.BOTH, expand=1)

def handler_ajouter():
    _tache = entree.get()
    if _tache:
        taches.ajouter(_tache)
        afficher_labels()

def fermer():
    print("Fermer l'interface")
    taches.db_fermer()
    fenetre.destroy()

fenetre.protocol("WM_DELETE_WINDOW", fermer)

frame = tk.Frame(fenetre)
entree = tk.Entry(frame, width=40)

btn_ajouter = tk.Button(frame, command=handler_ajouter, text="+", padx=10)
btn_supprimer = tk.Button(frame, text="-", padx=10)
btn_terminer = tk.Button(frame, text="x", padx=10)

frame.pack(pady=15)
entree.grid(row=0, column=0, ipady=4)
btn_ajouter.grid(row=0, column=1, padx=2)
btn_terminer.grid(row=0, column=2, padx=2)
btn_supprimer.grid(row=0, column=3, padx=2)
afficher_labels()
fenetre.mainloop()