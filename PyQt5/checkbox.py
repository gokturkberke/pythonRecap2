import sys
from PyQt5 import QtWidgets, QtGui

class Pencere(QtWidgets.QWidget): #miras almak icin qtwidgets.qwidget yazdik
    def __init__(self):
        super().__init__() #miras aldik init fonksiyonunu
        self.init_ui()
    def init_ui(self):
        self.onaykutusu=QtWidgets.QCheckBox("Uyelik sozlemesini okudum")
        self.etiket=QtWidgets.QLabel("")
        self.kayit_ol =QtWidgets.QPushButton("Kayit Ol")
        
        
        vb=QtWidgets.QVBoxLayout()
        vb.addStretch() #tum ogeleri alta atar
        vb.addWidget(self.onaykutusu)
        vb.addWidget(self.etiket)
        vb.addWidget(self.kayit_ol)
        
        self.setLayout(vb)
        
        self.kayit_ol.clicked.connect(lambda :self.tiklama(self.onaykutusu.isChecked())) #onay kutusuna tiklayip tiklamadigini kontrol eder
        self.show()
        
    def tiklama(self,onay_kutusu):
        if onay_kutusu: #ona kutusu secili ise
            self.etiket.setText("Kayit Basarili")
        else:
            self.etiket.setText("Sozlemeyi onaylayiniz")

obje = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setGeometry(100,100,400,300)
pencere.setWindowTitle("Uyelik Formu")
sys.exit(obje.exec_())