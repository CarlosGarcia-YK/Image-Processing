import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image_path = 'dos.jpg' #Path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error")

def piecewise_transform(image):
    # Segments
    value = np.zeros_like(image)
    
   
    part1 = (image >= 0) & (image < 80)
    value[part1] = np.interp(image[part1], [0, 80], [0, 5])
    
    part2 = (image >= 80) & (image < 115)
    value[part2] = np.interp(image[part2], [80, 115], [5, 100])
    
    
    part3 = (image >= 115) & (image <= 255)
    value[part3] = np.interp(image[part3], [115, 255], [100, 255])

    return value

def plot_transformation():
    # Inputs
    r = [0, 80, 115, 255]
    s = [0, 5, 100, 255]
    
    plt.figure(figsize=(8, 6))
    plt.plot(r, s, marker='o', linestyle='-', color='blue')
    plt.title('Piecewise')
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.grid(True)
    plt.xticks(range(0, 256, 20))
    plt.yticks(range(0, 256, 20))
    plt.axis([0, 255, 0, 255])
    plt.show()


transformed = piecewise_transform(image)
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()


plot_transformation()