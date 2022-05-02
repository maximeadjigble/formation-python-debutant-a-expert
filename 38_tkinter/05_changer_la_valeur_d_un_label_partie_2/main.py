import tkinter as tk

fenetre = tk.Tk()
 
def mon_bouton():
    # print("Cliqué!")
    val = val_compteur.get()
    val_compteur.set(int(val) + 1)
    # print(type(val_compteur.get()), val_compteur.get())
 
val_compteur = tk.StringVar(value="0")
label = tk.Label(textvariable=val_compteur)
 
bouton = tk.Button(
    command=mon_bouton, 
    text="Incrémenter",
    padx=10,
    pady=5,
)

label.pack() 
bouton.pack()
fenetre.mainloop() 