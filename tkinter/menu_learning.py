from tkinter import *

root = Tk( )
root.title("Menu Learning")
root.geometry("400x200+200+200")

menubar = Menu(root)
root.config(menu=menubar) 

file_menu = Menu(menubar) #Menu icindeki file menusunu olusturuyoruz
menubar.add_cascade(label="File", menu=file_menu) #File menusunu menubara ekliyoruz

def open_button():
    open_window=Toplevel()
    print("File opened")

def copy_button():
    print("File copied")

file_menu.add_command(label="Open",command=open_button) #File menusune open secenegi ekledik
#file_menu.add_command(label="Save") 
save_menu= Menu(file_menu)
file_menu.add_cascade(label="Save",menu=save_menu)
save_menu.add_command(label=".py")
save_menu.add_command(label=".txt")

file_menu.add_command(label="Exit",command=exit) 

edit_menu = Menu(menubar)
menubar.add_cascade(label="Edit", menu=edit_menu)   #Edit menusunu menubara ekliyoruz

edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy",command=copy_button)

root.mainloop()