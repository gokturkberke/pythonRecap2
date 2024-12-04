from tkinter import *

window = Tk()
window.title("Scale and Spinbox")
window.geometry("600x400+200+200")

#scale

def print_selection(value):
    print(value)

my_scale = Scale(from_=100, to=200,command=print_selection,label="volume")#orient = HORIZONTAL
my_scale.pack()

my_scale2 = Scale(from_=1, to=100,command=print_selection,label="bas")#orient = HORIZONTAL
my_scale.pack()

#spinbox

def spinbox_selected():
    print(my_spinbox.get())

my_spinbox=Spinbox(from_=0, to = 50,values=(0,5,10,15,20,25,30,35,40,45,50), command=spinbox_selected) #5 er 5 er artiyor spinboxumuz
my_spinbox.pack()

window.mainloop()