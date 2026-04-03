class calculator:
    """Calculator class for operations between two vectors."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Compute and print the dot product of two vectors."""
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise and print the result."""
        result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors element-wise and print the result."""
        result = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")


def main():
    """Test the calculator class with vector-vector operations."""
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
