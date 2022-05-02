import tkinter as tk

fenetre = tk.Tk()

def incrementer():
    # print(val_compteur.get(), type(val_compteur.get()))
    val = int(val_compteur.get())
    val_compteur.set(val + 1)

def decrementer():
    val = int(val_compteur.get())
    if val > 0:
        val_compteur.set(val - 1)

val_compteur = tk.StringVar(value="0")
nombre = tk.Label(textvariable=val_compteur, padx=50, pady=10)
btn_incr = tk.Button(command=incrementer, text="+", padx=20, pady=10)
btn_decr = tk.Button(command=decrementer,text="-", padx=20, pady=10)

btn_decr.grid(row=0, column=0)
nombre.grid(row=0, column=1)
btn_incr.grid(row=0, column=2)

# nombre.pack()
# btn_incr.pack()
# btn_decr.pack()
fenetre.mainloop()