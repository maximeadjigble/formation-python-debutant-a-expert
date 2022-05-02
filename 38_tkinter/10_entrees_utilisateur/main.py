import tkinter as tk

fenetre = tk.Tk()

def salutations():
    # print(entree.get())
    montexte = tk.Label(text=f"Bonjour {entree.get()}")
    montexte.pack()

# entree = tk.Entry(fg="white", bg="black", width=50)
entree = tk.Entry()
label = tk.Label(text="Prénom")
btn = tk.Button(
    command=salutations,
    text="saluer",
    padx=10
)

label.pack()
entree.pack()
btn.pack()
fenetre.mainloop() 