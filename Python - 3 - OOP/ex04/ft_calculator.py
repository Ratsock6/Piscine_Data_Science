class calculator:
    """Calculator class for operations between a vector and a scalar."""

    def __init__(self, lst: list):
        """Initialize the calculator with a list representing a vector."""
        self.lst = lst

    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector and print the result."""
        self.lst = [x + object for x in self.lst]
        print(self.lst)

    def __mul__(self, object) -> None:
        """Multiply each element of the vector by a scalar and print."""
        self.lst = [x * object for x in self.lst]
        print(self.lst)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element of the vector and print."""
        self.lst = [x - object for x in self.lst]
        print(self.lst)

    def __truediv__(self, object) -> None:
        """Divide each element of the vector by a scalar and print."""
        if object == 0:
            print("ERROR (dividing by zero is not allowed)")
            return
        self.lst = [x / object for x in self.lst]
        print(self.lst)


def main():
    """Test the calculator class with vector-scalar operations."""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
