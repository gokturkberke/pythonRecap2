import sys
from PyQt5 import QtWidgets, QtGui

obje = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setGeometry(200, 200, 400, 600)

save = QtWidgets.QPushButton() #Button
save.setText("Save") #Button Text

leave = QtWidgets.QPushButton()
leave.setText("Leave")

hb = QtWidgets.QHBoxLayout()#Horizontal Box
hb.addWidget(save)
hb.addWidget(leave)

# hb.addStretch() #Pencere boyutunu arttirsak bile butonlarin boyutu degismez

# window.setLayout(hb)

vb = QtWidgets.QVBoxLayout()#Vertical Box
#vb.addWidget(save)
#vb.addWidget(leave)

vb.addStretch()
vb.addLayout(hb) #Horizontal Box'u Vertical Box'a ekledik (alta yasili olur)

window.setLayout(vb)

window.show()
sys.exit(obje.exec_())