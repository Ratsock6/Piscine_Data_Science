import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be an RGB image (H, W, 3).")
    inverted = 255 - array
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Applies a red filter by keeping only the red channel."""
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be an RGB image (H, W, 3).")
    red = np.copy(array)
    red[..., 1] *= 0  # G
    red[..., 2] *= 0  # B
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """Applies a green filter by keeping only the green channel."""
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be an RGB image (H, W, 3).")
    green = np.copy(array)
    green[..., 0] -= green[..., 0]  # R → 0
    green[..., 2] -= green[..., 2]  # B → 0
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Applies a blue filter by keeping only the blue channel."""
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be an RGB image (H, W, 3).")
    blue = np.copy(array)
    blue[..., 0] = 0  # R
    blue[..., 1] = 0  # G
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale (average of RGB channels)."""
    if array.ndim != 3 or array.shape[2] != 3:
        raise AssertionError("Input must be an RGB image (H, W, 3).")
    grey = np.copy(array).astype(np.float64)
    mean = (grey[..., 0] + grey[..., 1] + grey[..., 2]) / 3
    grey[:, :, 0] = mean
    grey[:, :, 1] = mean
    grey[:, :, 2] = mean
    return grey.astype(np.uint8)


def ft_display(array: np.ndarray, title: str = "Image") -> None:
    """Displays an image using matplotlib with its title."""
    if array.ndim not in (2, 3):
        raise AssertionError("ft_display expects a 2D or 3D image array.")

    plt.imshow(array.astype(np.uint8))
    plt.title(title)
    plt.axis("off")
    plt.show()
