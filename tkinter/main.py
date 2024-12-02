from tkinter import *
# import tkinter

window = Tk() # Create a window
window.title("Python Tkinter")
window.geometry("600x400+200+200") # Set the window size(600 genislik 400 yukseklik )
#window.minsize(300,200) # Set the minimum window size(300 genislik 200 yukseklik)
#window.maxsize(800,600) # Set the maximum window size(800 genislik 600 yukseklik)
window.resizable(False,False) # Set the window to be resizable in x and y directions(ekrani boyutlandirmayi kapatir)

my_label = Label(text="This is a label") #calistirinca ekranda yazimiz daha gozukmez
my_label.pack() # Add the label to the window(simdi gozukur)


window.mainloop() # Start the window's main loop(kapanmamasini saglar)