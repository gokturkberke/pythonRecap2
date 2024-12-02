from tkinter import *

window = Tk()
window.title("Label Learning")
window.geometry("600x400")
my_label=Label(text="This is\n a label", 
               fg="light blue",
               bg="black",
               font="Arial 30 italic underline") #italic egik yapar biraz,underlnie altini cizer italic yerine bold yaparsak daha kalin olur...
my_label.pack()



window.mainloop()

