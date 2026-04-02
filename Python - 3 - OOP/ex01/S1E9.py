from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the character with a name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Set the character's alive status to False."""
        pass


class Stark(Character):
    """Class representing a member of the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character with a name and alive status."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the character by setting is_alive to False."""
        self.is_alive = False


def main():
    """Test the Character and Stark classes."""
    ned = Stark("Ned")
    print(ned.__dict__)
    print(ned.is_alive)
    ned.die()
    print(ned.is_alive)
    print(ned.__doc__)
    print(ned.__init__.__doc__)
    print(ned.die.__doc__)
    print("---")
    lyanna = Stark("Lyanna", False)
    print(lyanna.__dict__)


if __name__ == "__main__":
    main()
