from tkinter import *

window = Tk()
window.title("Listbox Example")
window.geometry("600x400")

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection())) # Getting the selected item from the listbox
# This function prints the currently selected item in the listbox

my_listbox=Listbox()

item_list = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5","Option 6"]

for i in range(len(item_list)):
    my_listbox.insert(i, item_list[i]) # Inserting items into the listbox

my_listbox.bind("<<ListboxSelect>>", listbox_selected) # Binding the listbox with the function
#This means that the listbox_selected function will be called whenever an item in the listbox is selected.
my_listbox.pack()

window.mainloop()