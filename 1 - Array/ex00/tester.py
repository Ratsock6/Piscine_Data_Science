from give_bmi import give_bmi, apply_limit

try:
    height = [1.75, 1.80, 1.65]
    weight = [70, 80, 60]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 25))
except Exception as e:
    print(f"Error: {e}")

try:
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except Exception as e:
    print(f"Error: {e}")
