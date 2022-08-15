import numpy as np
import pywt
import cv2

def wavelet2D(image, Wname="haar", level=1):
    # Convert image to grayscale.
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Covert to float.
    gray_image = np.float32(gray_image)
    # Scale the data to a 0-1 range.
    gray_image /=255
    
    # Compute coefficients!
    coeffs = pywt.wavedec2(gray_image, Wname, level=level)
    
    # Process coefficients!
    coeffs_p = list(coeffs)
    coeffs_p[0] *= 0  # Zero the Aproximation coefficient matrix.
    
    # Reconstructing the image with the processed coefficients.
    image_r = pywt.waverec2(coeffs_p, Wname)
    
    # Unscale!
    image_r *= 255
    
    # Convert data type.
    image_r = np.uint8(image_r)
    
    
    return image_r

# ifunanyaScript
