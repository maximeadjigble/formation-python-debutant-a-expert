import tkinter as tk
from generateur import generer

LONGEUR_DEFAUT = 10

fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe")
fenetre.geometry("250x100")

def generer_motdepasse():
    taille = int(entree.get())
    # print(generer(taille))
    if taille > 0 and taille < 20:
        motdepasse.set(generer(taille))
    else:
        motdepasse.set("La taille est incorrecte")

motdepasse = tk.StringVar(value="Mot de passe")
label_motdepasse = tk.Label(textvariable=motdepasse)

frame = tk.Frame()
label_entree = tk.Label(frame, text="Longeur")
entree = tk.Entry(frame)
entree.insert(0, LONGEUR_DEFAUT)
bouton = tk.Button(frame,command=generer_motdepasse, text="Générer")

label_motdepasse.pack(pady=20)
label_entree.grid(row=0, column=0)
entree.grid(row=0, column=1, padx=5)
bouton.grid(row=0, column=2)

frame.pack()
fenetre.mainloop()