from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog

class HoughGUI(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(HoughGUI, self).__init__()

        uic.loadUi("assets/design_v12.ui", self)

        self.init_elements()

        print("Interface is successfully loaded.")
        self.show()

    
    def init_elements(self):
        self.pushButton_browse.clicked.connect(self.browse_image)
        
    
    def browse_image(self):
        self.lineEdit.setText(QFileDialog.getOpenFileName())