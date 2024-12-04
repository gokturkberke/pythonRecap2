from tkinter import *

window = Tk()
window.title("Scrollbar Example")
#window.geometry("400x300+200+200")

my_scrollbar = Scrollbar() # orient=HORIZONTAL means the scrollbar will be horizontal
#my_scrollbar.pack(side=RIGHT,fill=Y) # fill=Y means the scrollbar will be vertical
my_scrollbar.pack(side=RIGHT,fill=Y) 


# my_text = Text(wrap=NONE,yscrollcommand=my_scrollbar.set) # wrap=NONE means the text will not wrap (alt satira inmeyecek satir doldugunda)
# my_text.pack()
mylist = Listbox(yscrollcommand=my_scrollbar.set,width=30,height=20)

for line in range(1,100):
    mylist.insert(END,"This is line number " + str(line))

mylist.pack(side=LEFT,fill=BOTH)

#my_scrollbar.config(command=my_text.yview) # scrollbari yukari asagi kaydirmak icin
my_scrollbar.config(command=mylist.yview) # scrollbari saga sola kaydirmak icin
window.mainloop()