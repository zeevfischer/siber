# this code will create an img of noise

# import numpy as np
# import cv2
#
# # Set the dimensions of your image
# width, height = 800, 600
#
# # Generate random noise (you can adjust the intensity by changing the scale)
# noise = np.random.normal(loc=0, scale=25, size=(height, width, 3))
#
# # Create an empty image and add the noise
# noise_img = np.zeros((height, width, 3), dtype=np.uint8)
# noise = noise.astype(np.uint8)  # Convert noise to uint8
# noise_img = cv2.addWeighted(noise_img, 1.0, noise, 1.0, 0)
#
# # Save or display the noise image
# cv2.imwrite('noise_image.png', noise_img)
# # or
# cv2.imshow('Noise Image', noise_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# this code takes an img and adds noise to it, but you don't see the change
# in this code the name of the output img is test 1.jpg
# the other path is to an img on my computer
from PIL import Image, ImageFilter
import numpy as np

def add_imperceptible_noise(image_path, output_path, intensity=1.0):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Generate imperceptible noise
    noise = np.random.normal(scale=intensity, size=img_array.shape)

    # Add noise to the image
    noisy_img_array = img_array + noise

    # Convert back to uint8 and create a new image
    noisy_img = Image.fromarray(np.uint8(noisy_img_array))

    # Save the result
    noisy_img.save(output_path)

# Example usage
add_imperceptible_noise(r"C:\Users\USER\Desktop\20160809_223425.jpg",'test1.jpg', intensity=0.1)
