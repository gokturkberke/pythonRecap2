from tkinter import *

window = Tk()
window.title("Label Learning")
window.geometry("600x400")
my_label=Label(text="This is\n a label", 
               fg="light blue",
               bg="black",
               font="Arial 30 italic underline") #italic egik yapar biraz,underlnie altini cizer italic yerine bold yaparsak daha kalin olur...
my_label.pack(side="left") 
#my_label.grid(row=0,column=0) #grid ile de konumlandirabiliriz sol ust koseye yer

def click_button():
    my_label.config(text="button clicked",fg="blue") #text degistirme

my_button = Button(text="Click me",command=click_button)#command=click_button butona tiklandiginda click_button fonksiyonunu calistirir
my_button.place(x=300,y=200)

my_label2 = Label(text="This is a label 2",
                 fg="#E7E241",
                 bg="gray",
                 font="Arial 30 bold underline")
my_label2.grid(row=1,column=1)
#my_label.place(x=100,y=100) #x ve y koordinatlarini belirler soldan 100 ustten 100
window.mainloop()

