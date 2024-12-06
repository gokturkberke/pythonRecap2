import sqlite3

veritabani = sqlite3.connect("veritabani.db") #olusturmak istedigimiz veri tabaninin ismini belirledik
imlec = veritabani.cursor() #imlec olusturduk

tablo_yap="CREATE TABLE IF NOT EXISTS personel (isim,soyisim,departman,maas)" 
imlec.execute(tablo_yap) #tablo olusturduk

veritabani.close()