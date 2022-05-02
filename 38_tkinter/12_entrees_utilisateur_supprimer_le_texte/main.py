import tkinter as tk

fenetre = tk.Tk()

entree = tk.Entry()
btn = tk.Button(
    command=lambda: entree.delete(0, tk.END),
    text="Supprimer",
    padx=10
)

entree.pack()
btn.pack()
fenetre.mainloop() 