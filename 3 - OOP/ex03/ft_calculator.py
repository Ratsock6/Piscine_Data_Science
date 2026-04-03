class calculator:
    """Calculator class for operations between a vector and a scalar."""

    def __init__(self, vector: list) -> None:
        """Initialize the calculator with a vector."""
        self.vector = vector

    def __add__(self, scalar) -> None:
        """Add a scalar to each element of the vector and print the result."""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar) -> None:
        """Multiply each element of the vector by a scalar and print the result."""
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar) -> None:
        """Subtract a scalar from each element of the vector and print the result."""
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar) -> None:
        """Divide each element of the vector by a scalar and print the result."""
        if scalar == 0:
            print("Error: division by zero")
            return
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)


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
