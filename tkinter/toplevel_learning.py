from tkinter import *
#ic ice pencereler
root = Tk()
root.title("Toplevel Learning")
root.geometry("400x300")

label1 = Label(root,text="This is root window")
label1.pack()

def add_window():
    top = Toplevel()
    top.geometry("200x100")
    top.title("Toplevel")

    label2 = Label(top,text="This is toplevel window") #top yazmazsak label2 de rootta calisir
    label2.pack()
    exit_button = Button(top,text="Close Window",command=top.destroy) # command=exit yaparsak root da kapanir
    exit_button.pack()

button = Button(root,text="Add Toplevel Window",command=add_window)
button.pack()

root.mainloop()
