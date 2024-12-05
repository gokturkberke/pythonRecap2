import sys
from PyQt5 import QtWidgets, QtGui

class Pencere(QtWidgets.QWidget): #miras almak icin qtwidgets.qwidget yazdik
    def __init__(self):
        super().__init__() #miras aldik init fonksiyonunu
        self.init_ui()
    def init_ui(self):
        self.buton = QtWidgets.QPushButton("Gorseli getir")
        self.gorsel = QtWidgets.QLabel("Gorsel gelecek")
        
        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.gorsel)
        vb.addWidget(self.buton)
        vb.addStretch()
        
        hb = QtWidgets.QHBoxLayout()
        hb.addStretch()
        hb.addLayout(vb)
        hb.addStretch()
        
        self.setLayout(hb)
        self.show()
        
        self.buton.clicked.connect(self.tiklama)
    
    def tiklama(self):
        self.gorsel.setPixmap(QtGui.QPixmap("key.png"))
        
obje = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setGeometry(100,100,500,500)

sys.exit(obje.exec_())
