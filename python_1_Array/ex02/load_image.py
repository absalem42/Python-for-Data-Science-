import numpy as np
from PIL import Image


def ft_load(path: str):
    """
    Load an image from the specified path and convert it to a NumPy array.

    Args:
        path (str): Path to the image file. Only files ending in
        .jpg or .jpeg are supported.

    Returns:
        numpy.ndarray: A 3D array of shape (height, width, 3)
        representing the RGB image.

    Raises:
        AssertionError: If the file extension is not .jpg or .jpeg.
        FileNotFoundError: If the image file does not exist at the given path.
        Exception: For any other errors encountered during loading
        or conversion.
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        img = Image.open(path)
        # print(img.format)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array

    except FileNotFoundError:
        print(f"Error: Image file not found at {str}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
