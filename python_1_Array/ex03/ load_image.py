import numpy as np
from PIL import Image
import os

def ft_load(path: str):
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        img = Image.open(path)
        # print(img.format)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array

        

        
    except FileNotFoundError:
        print(f"Error: Image file not found at {str}")
    except Exception as e:
        print(f"An error occurred: {e}")

