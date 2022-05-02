import tkinter as tk

fenetre = tk.Tk()

def salutations():
    entree.insert(3,"*INSERE*")
    # montexte = tk.Label(text=f"Bonjour {entree.get()}")
    # montexte.pack()

entree = tk.Entry()
entree.insert(0,"Benois")
btn = tk.Button(
    command=salutations,
    text="saluer",
    padx=10
)

entree.pack()
btn.pack()
fenetre.mainloop() 