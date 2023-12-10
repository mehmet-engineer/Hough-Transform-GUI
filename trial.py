import cv2
from ShapeDetector import ShapeDetector

detector = ShapeDetector()

detector.load_line_image("img_for_lines.png")
detector.preprocess_images()

num_lines, plotted_img = detector.detect_lines()
print(num_lines)

cv2.imshow("Window", plotted_img)
key = cv2.waitKey()
cv2.destroyAllWindows()