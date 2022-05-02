import tkinter as tk
from tkinter.font import Font

fenetre = tk.Tk()
fenetre.title("Calculatrice")

texte = tk.StringVar(value="0123456789.")
label = tk.Label(textvariable=texte, width=29, pady=20,
                borderwidth=2, relief="groove",
                font=Font(family= "Comic Sans MS", size=16, weight="bold"))
label.pack()

btn_texte = ['', '', 'C', '/', '7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '', '0', '.','=']

frame = tk.Frame()
k = 0
for i in range(5):
    for j in range(4):
        if k >= len(btn_texte):
            break
        btn = tk.Button(frame, text=btn_texte[k], padx=40, pady=20)
        btn.grid(row=i, column=j)
        k += 1

frame.pack()
fenetre.mainloop()