# zoom.py
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    try:
        # Make NumPy print like the subject (show ... in the middle)
        np.set_printoptions(edgeitems=3, threshold=15)

        # 1. Load the image
        img = ft_load("animal.jpeg")
        if img is None:
            print("Failed to load image.")
            return

        # 2. Print original shape and pixel content
        print("The shape of image is:", img.shape)
        print(img[:1, :, :])  # one row, all columns → shows ...

        # 3. Crop fixed 400x400 region (same as subject example)
        y_start, y_end = 100, 500
        x_start, x_end = 450, 850

        zoomed = img[y_start:y_end, x_start:x_end, 0:1]  # red channel only

        # 4. Print new shape and pixel content (match subject format)

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)  # one row, all columns → shows ...

        # 5. Display zoomed image with axes (scale shown)
        plt.imshow((zoomed), cmap="gray")
        plt.show()

    except KeyboardInterrupt:
        print("Interrupted by user (Ctrl+C). Closing and exiting.")
        plt.close("all")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
