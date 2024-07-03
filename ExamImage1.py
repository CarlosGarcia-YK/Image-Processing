import cv2
import numpy as np

def median_filter(image_path, kernel):
   
    image = cv2.imread(image_path)

    if image is None:
        print("Error")
        return
   
    blurred = cv2.medianBlur(image, kernel)

    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Median, image and filter 
median_filter('uno.jpg', 7)  #Change path here
