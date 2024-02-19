# this is a simple code that combines 2 images
# this was used to combine an img with a filter attack

import cv2
import numpy as np

def add_images(image1_path, image2_path, output_path):
    # Read the images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Ensure images are of the same size
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Add the images together
    result = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

    # Save or display the result
    cv2.imwrite(output_path, result)
    # or
    cv2.imshow('Combined Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
add_images(r"C:\Users\USER\Desktop\P1110564.JPG", r"C:\Users\USER\Desktop\output_image.jpg", 'output_image1.jpg')
