from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon with brown eyes and dark hair."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """Return a string representation of the Baratheon character."""
        return (
            f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        )

    def __repr__(self) -> str:
        """Return an official string representation of the Baratheon."""
        return (
            f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        )

    def die(self):
        """Kill the character by setting is_alive to False."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister with blue eyes and light hair."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Return a string representation of the Lannister character."""
        return (
            f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        )

    def __repr__(self) -> str:
        """Return an official string representation of the Lannister."""
        return (
            f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        )

    def die(self):
        """Kill the character by setting is_alive to False."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create and return a new Lannister instance via class method."""
        return cls(first_name, is_alive)


def main():
    """Test the Baratheon and Lannister classes."""
    robert = Baratheon("Robert")
    print(robert.__dict__)
    print(robert.__str__)
    print(robert.__repr__)
    print(robert.is_alive)
    robert.die()
    print(robert.is_alive)
    print(robert.__doc__)
    print("---")
    cersei = Lannister("Cersei")
    print(cersei.__dict__)
    print(cersei.__str__)
    print(cersei.is_alive)
    print("---")
    jaine = Lannister.create_lannister("Jaine", True)
    print(
        f"Name : {jaine.first_name, type(jaine).__name__},"
        f" Alive : {jaine.is_alive}"
    )


if __name__ == "__main__":
    main()
