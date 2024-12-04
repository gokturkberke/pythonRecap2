from tkinter import *

window = Tk() 
window.title("Python Tkinter")
window.geometry("600x400+200+200")

def click_clear_button():
    data_entry.delete(0,END) # 0. indexden basla ve sona kadar sil


def click_send_button():
    print("button clicked")
    data_input = data_entry.get() # entry icindeki veriyi al
    print(data_input)
    click_clear_button() #sendledikten sonra sil
    
def click_send_button2():
    text_content = text_input.get(1.0,END) #1. satir 0. sutundan  sona kadar al (satirlar 1 den baslar sutunlar 0 dan)
    print(text_content)

    
data_entry= Entry(width=30)
data_entry.pack()


clear_button = Button(text="Clear",width=20,command=click_clear_button)
clear_button.pack()


send_button = Button(text="Send",width=20,command=click_send_button)
send_button.pack(padx=10,pady=10)

text_input = Text(width=30,height=5,bg="light blue",fg="black")
text_input.focus() # text_inputa odaklanir imlec acildiginda orda olur
text_input.pack(padx=10,pady=10)

send_button2 = Button(text="Send",width=20,command=click_send_button2)
send_button2.pack(padx=10,pady=10)

window.mainloop()