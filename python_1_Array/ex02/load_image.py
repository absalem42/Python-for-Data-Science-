import numpy as np
from PIL import Image
import os

def ft_load(path: str):
    try:
        img = Image.open(path)
        print(img.format)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img_array = np.array(img)
        print(img_array.shape)


        print(f"Image size (width, height): {img.size}")
        print(f"Image format: {img.format}")
        print(f"Image mode: {img.mode}") 

        print(img_array[:1, :-5, :])
        

        
    except FileNotFoundError:
        print(f"Error: Image file not found at {str}")
    except Exception as e:
        print(f"An error occurred: {e}")




def main():
    print(ft_load("landscape.jpg"))





if __name__ == "__main__":
    main()