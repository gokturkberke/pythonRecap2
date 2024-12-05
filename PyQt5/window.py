#Tkinter ->Daha basit,Küçük kişisel projeler
#PyQt5 - > Daha karmaşık,Modern ve profesyonel projeler,
#PyQt5, Qt Framework'ün Python bağlamalarıdır. Qt, C++ ile yazılmış güçlü ve modern bir GUI framework'üdür
import sys
from PyQt5 import QtWidgets

obje = QtWidgets.QApplication(sys.argv) # Create an application object
window = QtWidgets.QWidget() # Create a window object

window.setWindowTitle("PyQt5 Window") # Set the window title
window.setGeometry(200,200,400,300) #400 300 boyutlarinda soldan ustten 200 bosluk var

etiket = QtWidgets.QLabel(window) # Create a label object
etiket.setText("Hello PyQt5") # Set the label text
etiket.move(200,150) # Move the label to the coordinates

window.show() # Show the window
sys.exit(obje.exec_()) # Close the application when the window is closed
#tkinterdaki window.mainloop() ile aynı işlevi görür.python3 window.py
