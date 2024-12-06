import os
import sys
from PyQt5 import QtWidgets

class Kelime_islemci(QtWidgets,QtWidgets):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QtWidgets.QTextEdit()
        self.ac = QtWidgets.QPushButton("Aç")
        self.kaydet= QtWidgets.QPushButton("Kaydet")
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.cikis = QtWidgets.QPushButton("Çıkış")
        
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.ac)
        hbox.addWidget(self.kaydet)
        hbox.addWidget(self.temizle)
        hbox.addWidget(self.cikis)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.yazi_alani)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.setWindowTitle("Kelime İşlemci Programi")
        
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
        self.temizle.clicked.connect(self.yazi_temizle)
        self.cikis.clicked.connect(self.cikis_yap)
        
        self.show()
    def dosya_ac(self):
        dosya = QtWidgets.QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("Desktop")) #os.getenv("HOME") ile kullanıcının desktop dizini alınır
        
        with open(dosya[0], "r") as file:
            self.yazi_alani.setText(file.read())
            
    def dosya_kaydet(self):
        dosya = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("Desktop")) #
        
        with open(dosya[0], "w") as file:
            file.write(self.yazi_alani.toPlainText()) #yazi_alani içindeki metni dosyaya yazdırır
    
    def yazi_temizle(self):
        self.yazi_alani.clear()
        
    def cikis_yap(self):
        quit()

obje = QtWidgets.QApplication(sys.argv)
kelimeIslemci= Kelime_islemci()
sys.exit(obje.exec_())


        
