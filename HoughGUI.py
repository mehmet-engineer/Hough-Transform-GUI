from ShapeDetector import ShapeDetector
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog

class HoughGUI(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(HoughGUI, self).__init__()

        uic.loadUi("assets/design_v12.ui", self)

        self.detector = ShapeDetector()

        self.init_elements()

        print("Interface is successfully loaded.")
        self.show()

    
    def init_elements(self):
        self.pushButton_browse.clicked.connect(self.browse_image)
        self.pushButton_load.clicked.connect(self.load_image)
        self.pushButton_process.clicked.connect(self.process_image)
        self.pushButton_clear.clicked.connect(self.clear_image)

        self.pushButton_process.setEnabled(False)
        self.pushButton_clear.setEnabled(False)
    
    def load_image(self):
        img_path = self.lineEdit.text()

        try:
            self.detector.load_line_image(img_path)
            pixmap = QPixmap(img_path)
            self.label_original_img.setPixmap(pixmap)
            self.label_original_img.setScaledContents(True)
            self.pushButton_process.setEnabled(True)
        except:
            QMessageBox.critical(self, "Error", "The image could not be loaded.")

        
        
    def process_image(self):
        self.detector.preprocess_images()
        num_lines, plotted_img = self.detector.detect_lines()

        rgb_img = self.detector.convert_to_rgb(plotted_img)

        h, w, c = rgb_img.shape
        bytesPerLine = c * w
        q_img = QImage(rgb_img.data, w, h, bytesPerLine, QImage.Format_RGB888)

        q_pixmap = QPixmap.fromImage(q_img)
        pixmap_img = QPixmap(q_pixmap)
        self.label_processed_img.setPixmap(pixmap_img)
        self.label_processed_img.setScaledContents(True)

        self.pushButton_clear.setEnabled(True)

    def clear_image(self):
        self.label_original_img.clear()
        self.label_processed_img.clear()

        self.pushButton_process.setEnabled(False)
        self.pushButton_clear.setEnabled(False)
    
    def browse_image(self):
        answer = QFileDialog.getOpenFileName()
        if answer is not None:
            self.lineEdit.setText(answer[0])