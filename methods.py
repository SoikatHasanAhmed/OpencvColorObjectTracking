import  cv2
import numpy as np

def find_marker(image):
    # convert the image to grayscale and blur to detect edges
    try:
        blurred_frame = cv2.GaussianBlur(image, (5, 5), 0)
        hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([38, 86, 0])
        upper_blue = np.array([121, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        con = max(contours, key=cv2.contourArea)

        return cv2.minAreaRect(con)
    except :
         return ((0.0, 0.0), (0.0, 0.0), 0.0)
