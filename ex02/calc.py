from gettext import bind_textdomain_codeset
from logging import root
import tkinter as tk

#練習1
root = tk.Tk()
root.geometry("300x500")

#練習2
r,c = 0,0
for i,num in enumerate(range(9,-1,-1),1):
    btn = tk.Button(root,text=f"{num}",font=("",30),width=4,height=2)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0


root.mainloop()