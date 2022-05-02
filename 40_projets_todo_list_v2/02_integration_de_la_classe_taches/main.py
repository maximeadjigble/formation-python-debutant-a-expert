import tkinter as tk
from taches import Taches

taches = Taches()
taches.db_connecter()
taches.afficher()
# taches.db_fermer()

fenetre = tk.Tk()
fenetre.title("Gestionnaire de taches")

def fermer():
    print("Fermer l'interface")
    taches.db_fermer()
    fenetre.destroy()

fenetre.protocol("WM_DELETE_WINDOW", fermer)

frame = tk.Frame(fenetre)
entree = tk.Entry(frame, width=40)

btn_ajouter = tk.Button(frame, text="+", padx=10)
btn_supprimer = tk.Button(frame, text="-", padx=10)
btn_terminer = tk.Button(frame, text="x", padx=10)

frame.pack(pady=15)
entree.grid(row=0, column=0, ipady=4)
btn_ajouter.grid(row=0, column=1, padx=2)
btn_terminer.grid(row=0, column=2, padx=2)
btn_supprimer.grid(row=0, column=3, padx=2)
fenetre.mainloop()