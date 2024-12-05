import sys
from PyQt5 import QtWidgets, QtGui

obje = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setGeometry(100, 100, 400, 400)

etiket = QtWidgets.QLabel(window)
etiket.setPixmap(QtGui.QPixmap("key.png")) #Resim dosyası
etiket.move(150,50)

dugme = QtWidgets.QPushButton(window)
dugme.setText("Tamam")
dugme.move(150,50)


window.show()
sys.exit(obje.exec_())