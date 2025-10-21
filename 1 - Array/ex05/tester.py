from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
from pimp_image import ft_display


def main():
    array = ft_load("landscape.jpg")

    invert = ft_invert(array)
    red = ft_red(array)
    green = ft_green(array)
    blue = ft_blue(array)
    grey = ft_grey(array)

    ft_display(array, "Original image")
    ft_display(invert, "Inverted colors")
    ft_display(red, "Red filter")
    ft_display(green, "Green filter")
    ft_display(blue, "Blue filter")
    ft_display(grey, "Grayscale")

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
