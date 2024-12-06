import sqlite3

veritabani=sqlite3.connect("veritabani.db")
imlec = veritabani.cursor()

tablo_yap = "CREATE TABLE IF NOT EXISTS personel (isim TEXT, soyisim TEXT, departman TEXT,maas INT)"

imlec.execute(tablo_yap) #eslestirme

veritabani.commit()#veritabanına kaydetme

imlec.execute("INSERT INTO personel VALUES ('Berke','Korkut','Yazılım',95000)")
imlec.execute("INSERT INTO personel VALUES ('Gokce','Korkut','Satin alma',65000)")
imlec.execute("INSERT INTO personel VALUES ('Aybala','Korkut','Insan kaynaklari',85000)")
veritabani.commit()

isim = input("Adiniz: ")
soyisim = input("Soyadiniz: ")
departman = input("Departmaniniz: ")
maas = int(input("Maasiniz: "))

imlec.execute("INSERT INTO personel VALUES (?,?,?,?)",(isim,soyisim,departman,maas))
veritabani.commit()

#tablodan verileri alma

def verileri_al():
    imlec.execute("SELECT * FROM personel")
    liste = imlec.fetchall() #fetchall() fonksiyonu veritabanındaki tüm verileri alır
    for i in liste: 
        print(i)


def kisileri_al(): #sadece isim ve soyisimleri almak icin
    imlec.execute("SELECT isim,soyisim FROM personel")
    liste = imlec.fetchall()
    for i in liste:
        print(i)
kisileri_al()

def departman_al():
    imlec.execute("SELECT * FROM personel where departman = 'Yazılım'") #departmanı yazılım olanları al
    liste = imlec.fetchall()
    for i in liste:
        print(i)
departman_al()

#verileri guncelleme silme
def guncelle(eski_departman,yeni_departman):
    imlec.execute("UPDATE personel set departman=? where departman=?",(yeni_departman,eski_departman)) #eski departmanı yeni departman yap
    #soru isaretleri eski departman ve yeni departman alır
    veritabani.commit()
    
guncelle('Yazılım','Yazılım Mühendisliği')

def sil(departman):
    imlec.execute("DELETE FROM personel where departman=?",(departman,))
    veritabani.commit()
sil('Satin alma')

verileri_al() 
veritabani.close()