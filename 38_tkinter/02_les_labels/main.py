import tkinter as tk
from tkinter.font import Font
from tkinter import font

fenetre = tk.Tk()
# print(font.families())
monlabel = tk.Label(text="Hello world",
                    # foreground="blue",
                    # background="#34A853",
                    fg="blue",
                    bg="#FA1056",
                    height=5,
                    width=20,
                    font=Font(family = "Comic Sans MS", size=30, weight="bold"))
monlabel.pack()

fenetre.mainloop()












