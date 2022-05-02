import tkinter as tk

fenetre = tk.Tk()
 
def mon_bouton():
    val = label.cget("text")
    label.configure(text=int(val) + 1)
    # print()
 
label = tk.Label(text="10")
 
bouton = tk.Button(
    command=mon_bouton, 
    text="Incrémenter",
    padx=10,
    pady=5,
)

label.pack() 
bouton.pack()
fenetre.mainloop() 