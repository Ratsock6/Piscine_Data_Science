import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices each sublist in a 2D list from 'start' to 'end' indices.

    Args:
        family (list): A 2D list where each sublist has the same length.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        list: A new 2D list with each sublist sliced from 'start' to 'end'.

    Raises:
        ValueError: If the input is not a 2D list or if sublists have
            different lengths.
    """
    # Vérification des types de base
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a list of lists")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    if len(family) == 0:
        raise ValueError("family cannot be empty")

    # Vérifie que toutes les sous-listes ont la même taille
    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise ValueError("All sublists in family must have the same length")

    # Conversion en tableau NumPy
    array = np.array(family, dtype=float)

    # Affiche la forme originale
    print(f"My shape is : {array.shape}")

    # Application du slicing
    new_array = array[start:end]

    # Affiche la nouvelle forme
    print(f"My new shape is : {new_array.shape}")

    # Retourne la nouvelle version en liste Python
    return new_array.tolist()
