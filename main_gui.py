import sys
from PyQt5 import QtWidgets
from HoughGUI import HoughGUI
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = HoughGUI()
    app.exec()
    sys.exit()