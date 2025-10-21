from __future__ import annotations

import sys
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def center_crop(arr: np.ndarray, crop_h: int, crop_w: int) -> np.ndarray:
    """
    Return a centered crop of size (crop_h, crop_w[, C]) from a 2D/3D array.

    Args:
        arr: Image array, shape (H, W) or (H, W, C).
        crop_h: Desired crop height.
        crop_w: Desired crop width.

    Raises:
        ValueError: If the crop is larger than the image.

    Returns:
        Cropped view of the array with same ndim as input.
    """
    if arr.ndim not in (2, 3):
        raise ValueError("Error: expected image with shape (H, W) or (H, W, C).")

    h, w = arr.shape[:2]
    if crop_h > h or crop_w > w:
        raise ValueError(
            f"Error: crop {crop_h}x{crop_w} does not fit inside image {h}x{w}."
        )

    y0 = (h - crop_h) // 2
    x0 = (w - crop_w) // 2
    return arr[y0 : y0 + crop_h, x0 : x0 + crop_w]


def rgb_to_grayscale(arr: np.ndarray) -> np.ndarray:
    """
    Convert an image to grayscale (H, W), accepting (H, W), (H, W, 3) or (H, W, 4).

    Uses luminance weights on the first three channels if present.

    Raises:
        ValueError: If array rank is not 2 or 3.
    """
    if arr.ndim == 2:
        gray = arr
    elif arr.ndim == 3:
        if arr.shape[2] < 3:
            raise ValueError("Error: expected at least 3 channels to make grayscale.")
        rgb = arr[..., :3].astype(np.float64)
        weights = np.array([0.2989, 0.5870, 0.1140], dtype=np.float64)
        # Grayscale = 0.2989×R + 0.5870×G + 0.1140×B
        gray = np.dot(rgb, weights)
    else:
        raise ValueError("Error: expected image with shape (H, W) or (H, W, C).")

    # Cast en uint8 si nécessaire
    if not np.issubdtype(gray.dtype, np.integer):
        gray = np.clip(gray, 0, 255).astype(np.uint8)
    return gray


def main() -> None:
    try:
        img = ft_load("animal.jpeg")
        print(img)

        cropped = center_crop(img, crop_h=400, crop_w=400)
        gray = rgb_to_grayscale(cropped)

        print(f"New shape after slicing: {gray.shape}")
        print(gray)
        arr_to_show = gray



        plt.figure()
        if arr_to_show.ndim == 2:
            plt.imshow(arr_to_show, cmap="gray", origin="upper")
        else:
            plt.imshow(arr_to_show.squeeze(-1), cmap="gray", origin="upper")
        plt.xlabel("X (px)")
        plt.ylabel("Y (px)")
        plt.title("Zoom 400×400")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(str(e), file=sys.stderr)


if __name__ == "__main__":
    main()
