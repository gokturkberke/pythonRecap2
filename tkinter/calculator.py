from tkinter import *

pencere = Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("400x300+300+100")
depo=""
pencere.resizable(width=False, height=False)

def hesapla(tus):
    global depo
    if tus in "0123456789":
        ekran.insert(END,tus) #ekrana tuslari yazdirir
        depo = depo + tus
    if tus in "+-*/":
        ekran.insert(END,tus)
        depo = depo + tus
    if tus == "=":
        ekran.delete(0,END)
        hesap = eval(depo,{"__builtins__":None},{}) # eval fonksiyonu string ifadeyi matematiksel ifadeye cevirir ve hesaplar
        depo = str(hesap)
        ekran.insert(END,depo)
    if tus == "C":
        ekran.delete(0,END)
        depo = ""
        
    
        

ekran = Entry(width=40,justify=RIGHT)
ekran.grid(row=0, column=0, columnspan=3,ipady=4) 
#columspan=3 3 kolon boyunca uzanacak, ipady=4 yukseklik ayarlamasi yazacagimiz yere ekler ipady yani widget icine
#pady olsa external padding it adds extra space outside

liste = ["1","2","3","4","5","6","7","8","9","0","+","-","/","*","=","C"]

row = 1
columns =0
for i in liste:
    komut = lambda x=i: hesapla(x)
    Button(text=i,font="Verdana 8 bold",bg="#FFFACD",width=10,height=2, relief=GROOVE,command=komut).grid(row=row, column=columns)
    columns +=1
    if columns >2:
        columns = 0
        row +=1
#relief = GROOVE butonun etrafina cizgi ceker,relief=raised(yukseltilmis sekilde disari dogru)

mainloop()