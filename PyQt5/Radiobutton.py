import sys
from PyQt5 import QtWidgets, QtGui

class Pencere(QtWidgets.QWidget): #miras almak icin qtwidgets.qwidget yazdik
    def __init__(self):
        super().__init__() #miras aldik init fonksiyonunu
        self.init_ui()
    def init_ui(self):
        self.soru = QtWidgets.QLabel("En cok sevdiginiz spor nedir?")
        self.futbol = QtWidgets.QRadioButton("Futbol")
        self.basketbol = QtWidgets.QRadioButton("Basketbol")
        self.voleybol = QtWidgets.QRadioButton("Voleybol")
        self.yuzme = QtWidgets.QRadioButton("Yuzme")
        
        self.etiket = QtWidgets.QLabel("")
        self.dugme=QtWidgets.QPushButton("Kaydet")
        
        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.soru)
        vb.addWidget(self.futbol)
        vb.addWidget(self.basketbol)
        vb.addWidget(self.voleybol)
        vb.addWidget(self.yuzme)
        vb.addStretch() # etiket dugme altta digerleri yukarda olur
        vb.addWidget(self.etiket)
        vb.addWidget(self.dugme)
        
        self.dugme.clicked.connect(lambda : self.tiklama(self.futbol.isChecked(),self.basketbol.isChecked(),self.voleybol.isChecked(),self.yuzme.isChecked(),self.etiket))
        
        self.setLayout(vb)#pencereye dahil etme
        self.show()
        
    def tiklama(self,futbol,basketbol,voleybol,yuzme,etiket):
        if futbol:
            self.etiket.setText("Futbol kaydedildi")
        if basketbol:
            self.etiket.setText("Basketbol kaydedildi")
        if voleybol:
            self.etiket.setText("Voleybol kaydedildi")
        if yuzme:
            etiket.setText("Yuzme kaydedildi")
    
        
obje = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setGeometry(100,100,500,500)
pencere.setWindowTitle("Radio Button")
sys.exit(obje.exec_())
