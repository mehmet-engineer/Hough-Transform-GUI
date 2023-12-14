import cv2
import numpy as np

class ShapeDetector():

    def __init__(self):
        self.line_img_path = ""
        self.original_line_img = None
        self.img_for_lines = None
        self.img_line_flag = False
        self.is_line_img_proccessed = False

    def load_line_image(self, file_path):
        self.line_img_path = file_path
        self.original_line_img = cv2.imread(self.line_img_path)
        self.img_for_lines = self.original_line_img.copy()
        self.img_line_flag = True

    def preprocess_images(self):
        
        # prepare variables
        k_size = (5,5)
        
        if self.img_line_flag == True:

            # if image is loaded, convert it to gray channel
            self.img_for_lines = cv2.cvtColor(self.img_for_lines, cv2.COLOR_BGR2GRAY)

            # blur and make smooth image
            self.img_for_lines = cv2.GaussianBlur(self.img_for_lines, k_size, 0)

            # detect canny edges
            self.img_for_lines = cv2.Canny(self.img_for_lines, threshold1=150, threshold2=200)

            self.is_line_img_proccessed = True


    def detect_lines(self) -> list:
        if self.is_line_img_proccessed == True:
            img = self.original_line_img.copy()
            lines = cv2.HoughLinesP(self.img_for_lines, 1, np.pi/180, 100, minLineLength=10, maxLineGap=20)
            if lines is not None:
                for line in lines:  
                    for x1,y1,x2,y2 in line:
                        cv2.line(img, (x1,y1), (x2,y2), [255,0,0], 2)
            return [len(lines), img]
    