import tkinter as tk

fenetre = tk.Tk()

def ma_fonction():
    # print("Cliqué!")
    montexte = tk.Label(text="Cliqué!")
    montexte.pack()

bouton = tk.Button(text="Mon bouton",
                    # command=ma_fonction,
                    command=lambda : tk.Label(text="Cliqué").pack(),
                    # bd=10,
                    fg="blue",
                    bg="#DC3545",
                    padx=20,
                    pady=10)
bouton.pack()

fenetre.mainloop()












