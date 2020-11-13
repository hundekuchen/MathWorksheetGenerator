#!/usr/---bin/python3

from tkinter import *
import sympy as sp
from PIL import Image, ImageTk
from io import BytesIO

class Root():
    def __init__(self, master):
        #Define the main window and the relevant widgets
        self.master = master
        master.geometry("800x300")
        self.label = Label(master)
        self.button = Button(text = "LaTeX!", command = self.on_latex)
        self.listbox = Listbox(master)
        self.listbox.insert(1,"3+\pi")
        self.listbox.insert(2,"4-\int")
        self.listbox.bind('<Double-1>', self.on_latex)       
        #grid everything
        self.label.grid(row=2, column=0)
        self.listbox.grid(row=3,column=0)
        
    def on_latex(self,event):
        cs=self.listbox.curselection()
        latex_string = self.listbox.get(cs)
        print(latex_string)
        expr = "$\displaystyle " + latex_string + "$"

        #This creates a ByteIO stream and saves there the output of sympy.preview
        f = BytesIO()
        the_color = "{" + self.master.cget('bg')[1:].upper()+"}"
        sp.preview(expr, euler = False, preamble = r"\documentclass{standalone}"
                   r"\begin{document}",
                   viewer = "BytesIO", output = "ps", outputbuffer=f)
        f.seek(0)
        #Open the image as if it were a file. This works only for .ps!
        img = Image.open(f)
        #See note at the bottom
        img.load(scale = 10)
        img = img.resize((int(img.size[0]/4),int(img.size[1]/4)),Image.BILINEAR)
        photo = ImageTk.PhotoImage(img)
        self.label.config(image = photo)
        self.label.image = photo
        f.close()
        
master = Tk()
root   = Root(master)
master.mainloop()