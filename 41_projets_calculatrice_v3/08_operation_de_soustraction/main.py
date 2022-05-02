import tkinter as tk
from tkinter.font import Font

fenetre = tk.Tk()
fenetre.title("Calculatrice")

texte = tk.StringVar(value="")
label = tk.Label(textvariable=texte, width=29, pady=20,
                borderwidth=2, relief="groove",
                font=Font(family= "Comic Sans MS", size=16, weight="bold"))
label.pack()

resultat = None
operation = None
def handler_click(event):
    val = event.widget.cget("text").strip()
    if not val:
        return
    if val in "0123456789.":
        if val == '.' and val in texte.get():
            return
        texte.set(texte.get() + val)
    else:
        global resultat
        global operation
        if val == 'C':
            texte.set('')
            resultat = None
            return

        nombre = int(texte.get()) if '.' not in texte.get() else float(texte.get())

        if val == '+':
            operation = '+'
            resultat = resultat + nombre if resultat else nombre
            texte.set("")
        elif val == "-":
            operation = '-'
            resultat = resultat - nombre if resultat else nombre
            texte.set("")            

        if val == "=":
            if operation == '+':
                texte.set(resultat + nombre)
            if operation == '-':
                texte.set(resultat - nombre)
            resultat = None
 

btn_texte = ['  ', '  ', 'C', '/', '7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '  ', '0', '.','=']

k = 0
btns = {}
frame = tk.Frame()
for i in range(5):
    for j in range(4):
        if k >= len(btn_texte):
            break
        val = btn_texte[k]
        btn = tk.Button(frame, text=val, padx=40, pady=20)
        btns[val] = btn
        btns[val].bind("<Button-1>", handler_click)
        btn.grid(row=i, column=j)
        k += 1

btns['C'].configure(padx=39)
btns['-'].configure(padx=41)
btns['.'].configure(padx=41)

frame.pack()
fenetre.mainloop()