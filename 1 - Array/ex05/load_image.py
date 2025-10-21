import os
import numpy as np
from numpy import array
from PIL import Image


def ft_load(path: str) -> array:
    """
    Load an image from the specified path and return it as a NumPy array.

    Parameters:
    path (str): The path to the image file to be loaded.

    Returns:
    np.ndarray: A NumPy array representing the loaded image.

    Raises:
    AssertionError: If the image format is wrong or the file is not found.

    Loads an image from the given path and performs checks to ensure
    compatibility and validity. Only JPG and JPEG formats are supported. If the
    file does not exist or the format is not supported, an Error is raised.
    The image is then converted to a NumPy array and its shape is printed.
    """
    if not path.lower().endswith(("jpg", "jpeg")):
        raise AssertionError("Only JPG and JPEG formats are supported.")
    if not os.path.exists(path):
        raise AssertionError("File not found:", path)
    img = Image.open(path)
    if img is None:
        raise AssertionError("Failed to load image.")
    arr = np.array(img)
    h, w = arr.shape[:2]
    c = arr.shape[2] if arr.ndim == 3 else 1
    print(f"The shape is: ({h}, {w}, {c})")
    return arr
