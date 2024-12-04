from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tkinter Learning")
root.geometry("400x300+200+200")

def click_message_button():
    #Information Message Box
    messagebox.showinfo("showinfo","This is Information Message Box")#title,message
    #Warning Message Box
    messagebox.showwarning("showwarning","This is Warning Message Box")
    #Error Message Box
    messagebox.showerror("showerror","This is Error Message Box")
    
    #Ask Question Message Box
    messagebox.askquestion("askquestion","Are you sure") #yes or no
    #Ask Ok Cancel Message Box
    messagebox.askokcancel("askokcancel","Want to continue") #ok or cancel
    #Ask Yes No Message Box
    messagebox.askyesno("askyesno","Do you want to exit") #yes or no
    #Ask Retry Cancel Message Box
    messagebox.askretrycancel("askretrycancel","Try again") #retry or cancel
    #Ask Yes No Cancel Message Box
    messagebox.askyesnocancel("askyesnocancel","Do you want to save") #yes or no or cancel

message_button = Button(text="Message",command=click_message_button)
message_button.pack()


root.mainloop()