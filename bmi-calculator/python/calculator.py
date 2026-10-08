def bmiCalculator(weight, height):
    bmi = weight / (height / 100) ** 2;
    return f"Your BMI is {bmi}"
