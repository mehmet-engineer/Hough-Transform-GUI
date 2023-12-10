import cv2
import numpy as np

class ShapeDetector():

    def __init__(self):
        self.line_img_path = ""
        self.circle_img_path = ""

        self.original_line_img = None
        self.original_circle_img = None

        self.img_for_lines = None
        self.img_for_circles = None
        
        self.img_line_flag = False
        self.img_circle_flag = False
        
        self.is_line_img_proccessed = False
        self.is_line_circle_proccessed = False

    def load_line_image(self, file_path):
        self.line_img_path = file_path
        self.original_line_img = cv2.imread(self.line_img_path)
        self.img_for_lines = self.original_line_img.copy()
        self.img_line_flag = True
    
    def load_circle_image(self, file_path):
        self.circle_img_path = file_path
        self.original_circle_img = cv2.imread(self.circle_img_path)
        self.img_for_circles = self.original_circle_img.copy()
        self.img_circle_flag = True

    def preprocess_images(self):
        
        # prepare variables
        k_size = (3,3)
        
        if self.img_line_flag == True:

            # if image is loaded, convert it to gray channel
            self.img_for_lines = cv2.cvtColor(self.img_for_lines, cv2.COLOR_BGR2GRAY)

            # blur and make smooth image
            self.img_for_lines = cv2.GaussianBlur(self.img_for_lines, k_size, 0)

            # detect canny edges
            self.img_for_lines = cv2.Canny(self.img_for_lines, threshold1=100, threshold2=200)

            self.is_line_img_proccessed = True

        
        if self.img_circle_flag == True:
            self.img_for_circles = cv2.cvtColor(self.img_for_circles, cv2.COLOR_BGR2GRAY)
            self.img_for_lines = cv2.GaussianBlur(self.img_for_lines, k_size, 0)
            self.img_for_circles = cv2.Canny(self.img_for_circles, threshold1=20, threshold2=300)
            self.is_circle_img_proccessed = True


    def detect_lines(self) -> list:
        if self.is_line_img_proccessed == True:
            img = self.original_line_img.copy()
            lines = cv2.HoughLinesP(self.img_for_lines, 1, np.pi/180, 100, minLineLength=28, maxLineGap=30)
            if lines is not None:
                for line in lines:  
                    for x1,y1,x2,y2 in line:
                        cv2.line(img, (x1,y1), (x2,y2), [255,0,0], 3)
            return [len(lines), img]
    
    def detect_circles(self) -> [int, list]:
        pass