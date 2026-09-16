from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing the King, mixing Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the King, using Baratheon as primary parent (MRO)."""
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> str:
        """Return the current eye color of the King."""
        return self.__dict__["eyes"]

    def set_eyes(self, color: str) -> None:
        """Set the eye color of the King."""
        self.__dict__["eyes"] = color

    def get_hairs(self) -> str:
        """Return the current hair color of the King."""
        return self.__dict__["hairs"]

    def set_hairs(self, color: str) -> None:
        """Set the hair color of the King."""
        self.__dict__["hairs"] = color

    eyes = property(get_eyes, set_eyes)
    hairs = property(get_hairs, set_hairs)


def main():
    """Test the King class with diamond inheritance."""
    joffrey = King("Joffrey")
    print(joffrey.__dict__)
    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")
    print(joffrey.get_eyes())
    print(joffrey.get_hairs())
    print(joffrey.__dict__)


if __name__ == "__main__":
    main()
