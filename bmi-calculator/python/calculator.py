# This is an example, not scientific advice
def bmiStatus(bmi):
    if bmi >= 40:
        return "obesity_class_3"
    elif bmi >= 35:
        return "obesity_class_2"
    elif bmi >= 30:
        return "obesity_class_1"
    elif bmi >= 25:
        return "overweight"
    elif bmi >= 18.5:
        return "normal"
    else:
        return "underweight"

def bmiCalculator(weight, height):
    return weight / (height / 100) ** 2;
