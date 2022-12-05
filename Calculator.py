from tkinter import *
from playsound import playsound as ps

root = Tk()
root.tk_setPalette("#E5B8F4")
root.title("Calculator")
root.iconbitmap("files/logo.ico")
root.geometry("289x420")
root.maxsize(289,420)
root.minsize(289,420)
e = Entry(root, width=45, borderwidth=8)
e.grid(row=0,column=0,columnspan=3)

def num(number):
    ps(f"files/{number%6}.mp3",block=False)
    current = e.get()
    e.delete(0,END)
    e.insert(0,f"{current}{number}")

def clr():
    e.delete(0,END)

def sum():
    global symbol
    symbol = "+"
    first = e.get()
    global memory
    memory = int(first)
    e.delete(0,END)   

def subtract():
    global symbol
    symbol="-"
    first = e.get()
    global memory
    memory = int(first)
    e.delete(0,END)  

def mult():
    global symbol
    symbol="*"
    first = e.get()
    global memory
    memory = int(first)
    e.delete(0,END)  

def divi():
    global symbol
    symbol="/"
    first = e.get()
    global memory
    memory = int(first)

def eq():
    ps("files/equal.mp3", block=False)
    sec = e.get()
    e.delete(0,END)
    if symbol=="+":
        e.insert(0, memory +int(sec))
    if symbol=="-":
        e.insert(0, memory -int(sec))
    if symbol=="*":
        e.insert(0, memory *int(sec))
    if symbol=="/":
        e.insert(0, memory /int(sec))

def dark():
    root.tk_setPalette("#000000")
    global bcolor
    global clrcolor
    bcolor = clrcolor= "black"
    global fcolor
    fcolor = "white"


def dflt():
    ps("files/equal.mp3", block=False)
    root.tk_setPalette("#E5B8F4")
    global bcolor
    bcolor = "violet"
    global clrcolor
    clrcolor = "#C147E9"
    global fcolor
    fcolor = "black"
dark()
ext = Button(root, text="EXIT", padx=32, pady=6, command=exit, fg=fcolor, bg="red", borderwidth=2)
num1 = Button(root, text="1", padx=40, pady=20, command=lambda :num(1), fg=fcolor, bg=bcolor, borderwidth=2)
num2 = Button(root, text="2", padx=40, pady=20, command=lambda :num(2), fg=fcolor, bg=bcolor, borderwidth=2)
num3 = Button(root, text="3", padx=40, pady=20, command=lambda :num(3), fg=fcolor, bg=bcolor, borderwidth=2)
num4 = Button(root, text="4", padx=40, pady=20, command=lambda :num(4), fg=fcolor, bg=bcolor, borderwidth=2)
num5 = Button(root, text="5", padx=40, pady=20, command=lambda :num(5), fg=fcolor, bg=bcolor, borderwidth=2)
num6 = Button(root, text="6", padx=40, pady=20, command=lambda :num(6), fg=fcolor, bg=bcolor, borderwidth=2)
num7 = Button(root, text="7", padx=40, pady=20, command=lambda :num(7), fg=fcolor, bg=bcolor, borderwidth=2)
num8 = Button(root, text="8", padx=40, pady=20, command=lambda :num(8), fg=fcolor, bg=bcolor, borderwidth=2)
num9 = Button(root, text="9", padx=40, pady=20, command=lambda :num(9), fg=fcolor, bg=bcolor, borderwidth=2)
num0 = Button(root, text="0", padx=40, pady=20, command=lambda :num(0), fg=fcolor, bg=bcolor, borderwidth=2)
add = Button(root, text="+", padx=39, pady=20, command=sum, fg=fcolor, bg=bcolor, borderwidth=2)
sub = Button(root, text="-", padx=41, pady=20, command=subtract, fg=fcolor, bg=bcolor, borderwidth=2)
mul = Button(root, text="x", padx=40, pady=20, command=mult, fg=fcolor, bg=bcolor, borderwidth=2)
div = Button(root, text="/", padx=40, pady=20, command=divi, fg=fcolor, bg=bcolor, borderwidth=2)
equal = Button(root, text="=", padx=39, pady=20, command=eq, fg=fcolor, bg=bcolor, borderwidth=2)
clear = Button(root, text="Clear", padx=126, pady=6, command=clr, fg=fcolor, bg=clrcolor, borderwidth=2)
drk = Button(root, text="Dark Space", padx=16, pady=6, command=dark, fg="white", bg="black", borderwidth=2)
de = Button(root, text="Default", padx=24, pady=6, command=dflt, fg="white", bg=bcolor, borderwidth=2)

ext.grid(row=7,column=2,columnspan=1)
num0.grid(row=4,column=0)
num1.grid(row=3,column=0)
num2.grid(row=3,column=1)
num3.grid(row=3,column=2)
num4.grid(row=2,column=0)
num5.grid(row=2,column=1)
num6.grid(row=2,column=2)
num7.grid(row=1,column=0)
num8.grid(row=1,column=1)
num9.grid(row=1,column=2)
add.grid(row=4,column=1)
clear.grid(row=6,column=0,columnspan=3)
equal.grid(row=5,column=0)
mul.grid(row=5,column=1)
div.grid(row=5,column=2)
sub.grid(row=4,column=2)
de.grid(row=7,column=0)
drk.grid(row=7,column=1)

root.mainloop()