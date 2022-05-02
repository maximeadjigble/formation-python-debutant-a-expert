import tkinter as tk

fenetre = tk.Tk()
label1 = tk.Label(text="Label1", bg="red")
label2 = tk.Label(text="Label2", bg="green")
label3 = tk.Label(text="Label3", bg="orange")
label4 = tk.Label(text="Label4", bg="violet")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
label4.grid(row=1, column=1)

# label1.pack() #tk.LEFT, side=tk.TOP, side=tk.RIGHT, side=tk.BOTTOM
# label2.pack() 
# label3.pack() 
# label4.pack() 
fenetre.mainloop() 