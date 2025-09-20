import numpy as np
from PIL import Image
import os

def ft_load(path: str):
    """
        Loads an image from the given path, converts it to RGB if necessary,
        and returns the image as a NumPy array.

        Parameters:
        - path (str): The path to the image file.

        Returns:
        - numpy.ndarray: The image represented as a NumPy array with RGB channels.

        Raises:
        - AssertionError: If the file is not in JPG or JPEG format.
        - FileNotFoundError: If the image file cannot be found at the given path.
    """

    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        img = Image.open(path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img_array = np.array(img)
        return img_array
        
    except FileNotFoundError:
        print(f"Error: Image file not found at {path}")
    except Exception as e:
        print(f"An error occurred: {e}")
