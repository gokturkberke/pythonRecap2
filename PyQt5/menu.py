import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        menubar = self.menuBar() # menubar olusturduk
        dosya = menubar.addMenu("Dosya") # menubar'a dosya adinda bir menu ekledik
        duzenle = menubar.addMenu("Duzenle") # menubar'a duzenle adinda bir menu ekledik
        
        ac = QAction("Ac",self) # ac adinda bir action olusturduk
        ac.setShortcut("Ctrl+O") # kisayol belirledik
        
        kaydet = QAction("Kaydet",self) # kaydet adinda bir action olusturduk
        kaydet.setShortcut("Ctrl+S") # kisayol belirledik
        
        cikis = QAction("Cikis",self) # cikis adinda bir action olusturduk
        cikis.setShortcut("Ctrl+Q") # kisayol belirledik
        
        dosya.addAction(ac) # dosya menu'sune ac action'ini ekledik
        dosya.addAction(kaydet)
        dosya.addAction(cikis)
        
        self.setWindowTitle("Menu olusturma")
        self.show()
        
        ekle = duzenle.addMenu("Ekle") # duzenle menu'sune ekle adinda bir menu ekledik
        
        sayfa = QAction("Sayfa",self) # sayfa adinda bir action olusturduk
        resim = QAction("Resim",self) # resim adinda bir action olusturdukq
        
        ekle.addAction(sayfa) # ekle menu'sune sayfa action'ini ekledik
        ekle.addAction(resim)
        
        cikis.triggered.connect(self.cikis_yap) # cikis action'una tiklandiginda cikis_yap fonksiyonunu cagir
        dosya.triggered.connect(self.tiklama)
        
    def cikis_yap(self):
        qApp.quit()
    
    def tiklama(self,action):
        if action.text() == "Ac":
            print("Ac'a tiklandi")
        elif action.text() == "Kaydet":
            print("Kaydet'e tiklandi")
        




obje = QApplication(sys.argv)
menu = Menu()
sys.exit(obje.exec_())