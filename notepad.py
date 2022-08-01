import tkinter
from tkinter import *
import os
from tkinter.messagebox import *
from tkinter.filedialog import *

title="Untitled Notepad"
root=Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")

def exit():
    if len(str(text.get(0.0,END)))==1:
        root.destroy()
    else:
        confirm = askyesnocancel("Notepad", "Do You want to save?")
        if confirm ==True:
            saveas()
            root.destroy()
        elif confirm==None:
            print("Cancelled")
        else:
            root.destroy()

def new():
    if len(str(text.get(0.0,END)))==1:
        text.delete(1.0,END)
    else:
        confirm = askyesnocancel("Notepad", "Do You want to save?")
        if confirm ==True:
            saveas()
        elif confirm==None:
            print("Cancelled")
        else:
            text.delete(1.0,END)

def save():
    file= open(text_file,'r+')
    text2save=str(text.get(0.0,END))
    file.write(text2save)

def saveas():
    global text_file
    text_file=asksaveasfile(initialdir="C:/Users/xXDarkLordXx/Documents", mode='w',defaultextension=".txt")
    text2save=str(text.get(0.0,END))
    text_file.write(text2save)

def opn():
    global text_file
    text_file = askopenfilename(initialdir="C:/Users/xXDarkLordXx/Documents", title="Open Text File", defaultextension=".txt",
                                  filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

    if text_file == "":

        text_file = None
    else:

        root.title(os.path.basename(text_file) + " - Notepad")
        text.delete(1.0,END)
        file= open(text_file,'r')
        stuff = file.read()
        text.insert(END, stuff)
        file.close()

def showAbout():
    showinfo("Notepad","Notepad by Devansh Jaiswal")

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")


menubar= Menu(root)
root.config(menu=menubar)

text=Text(root,width = 600,height=400,font=("Helvetica",16))
text.pack()

mymenufile= Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=mymenufile)
mymenufile.add_command(label="New File",command = new)
mymenufile.add_command(label="Open",command = opn)
mymenufile.add_command(label="Save",command = save)
mymenufile.add_command(label="Save As",command = saveas)
mymenufile.add_separator()
mymenufile.add_command(label="Exit",command = exit)

mymenuedit= Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=mymenuedit)
mymenuedit.add_command(label="Cut",command= cut)
mymenuedit.add_command(label="Copy",command=copy)
mymenuedit.add_command(label="Paste",command=paste)

mymenuhelp= Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help",menu=mymenuhelp)
mymenuhelp.add_command(label="About Notepad",command=showAbout)

root.mainloop()
