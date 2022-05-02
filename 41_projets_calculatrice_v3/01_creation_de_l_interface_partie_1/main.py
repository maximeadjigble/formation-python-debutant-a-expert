import tkinter as tk
from tkinter.font import Font

fenetre = tk.Tk()
fenetre.title("Calculatrice")

texte = tk.StringVar(value="0123456789.")
label = tk.Label(textvariable=texte, width=29, pady=20,
                borderwidth=2, relief="groove",
                font=Font(family= "Comic Sans MS", size=16, weight="bold"))

label.pack()
fenetre.mainloop()