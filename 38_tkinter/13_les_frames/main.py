import tkinter as tk

fenetre = tk.Tk()

frame = tk.LabelFrame(fenetre, text="Mes commandes", padx=50, pady=50)
label = tk.Label(frame, text="Mon label")
btn = tk.Button(frame,
    text="OK",
    padx=10,
)

label2 = tk.Label(text="Mon label 2")
label.grid(row=0, column=0)
btn.grid(row=0, column=1)
frame.pack()
label2.pack()
fenetre.mainloop() 