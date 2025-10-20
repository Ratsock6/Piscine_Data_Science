import numpy as np

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Compute BMI (Body Mass Index) for each pair of height and weight.
    Returns a list of float values.
    """
    # Vérifications de type
    if (len(height) != len(weight)):
        raise ValueError("height and weight lists must have the same length")
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("height list must contain only int or float values")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("weight list must contain only int or float values")
    # Utilisation de numpy pour le calcul du BMI
    height_array = np.array(height)
    weight_array = np.array(weight)
    bmi = weight_array / (height_array ** 2)
    return bmi.tolist()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare each BMI value to a given limit and return a list of booleans.

    Args:
        bmi (list[int | float]): A list of Body Mass Index (BMI) values.
        limit (int): The numerical limit to compare against.

    Returns:
        list[bool]: A list where each element is True if the corresponding
        BMI value is greater than the limit, otherwise False.

    Raises:
        TypeError: If bmi is not a list, or if it contains non-numeric values,
                   or if limit is not an int or float.
        ValueError: If the list bmi is empty.
    """
    # Vérifications de type
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise TypeError("bmi list must contain only int or float values")
    if not isinstance(limit, (int, float)):
        raise TypeError("limit must be an int or float")

    # Vérification de contenu
    if len(bmi) == 0:
        raise ValueError("bmi list cannot be empty")

    # Comparaison logique
    return [x > limit for x in bmi]
