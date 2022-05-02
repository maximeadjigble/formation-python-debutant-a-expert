import tkinter as tk
from PIL import ImageTk, Image

fenetre = tk.Tk()
image = ImageTk.PhotoImage(Image.open("paris.jpg"))
label = tk.Label(image=image)
label.pack()
fenetre.mainloop() 