from tkinter import *

window = Tk()
window.title("Python Tkinter")
window.geometry('600x400+200+200')

def checkbutton_selected():
    print(check_state.get())
    
#checkbutton
check_state=IntVar()#tiklandiginda sayisal olarak 1 veya 0 degeri uretir
my_checkbutton = Checkbutton(text="Check",variable=check_state,command=checkbutton_selected)
my_checkbutton.pack()

#radiobutton
def radioselected():
    print(radio_check_state.get())

radio_check_state = IntVar()
my_radiobutton = Radiobutton(text="Option 1", value = 100,variable =radio_check_state,command=radioselected)
my_radiobutton2 = Radiobutton(text="Option 2", value = 200,variable =radio_check_state,command=radioselected)
my_radiobutton.pack()
my_radiobutton2.pack()

window.mainloop()
