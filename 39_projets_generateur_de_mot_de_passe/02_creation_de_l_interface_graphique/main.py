import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe")
fenetre.geometry("250x100")

motdepasse = tk.StringVar(value="Mot de passe")
label_motdepasse = tk.Label(textvariable=motdepasse)

frame = tk.Frame()
label_entree = tk.Label(frame, text="Longeur")
entree = tk.Entry(frame)
bouton = tk.Button(frame, text="Générer")

label_motdepasse.pack(pady=20)
label_entree.grid(row=0, column=0)
entree.grid(row=0, column=1, padx=5)
bouton.grid(row=0, column=2)

frame.pack()
fenetre.mainloop()