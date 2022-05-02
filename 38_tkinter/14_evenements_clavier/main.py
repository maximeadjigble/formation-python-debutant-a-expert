import tkinter as tk

fenetre = tk.Tk()

def ma_fonction(event):
    # print(event)
    print(f"Souris x: {event.x} y: {event.y} - Touche: {event.keysym}")

fenetre.bind("<Button-1>",ma_fonction)
fenetre.mainloop() 