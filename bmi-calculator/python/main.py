import calculator

while True:
    userChoice = input("Welcome to BMI calculator, please make your choice [1] KG and CM, [2] Lb and Ft [q]: ")
    if userChoice == "1":
        print("Mode: KG and CM")
        weight = float(input("Enter your weight: "))
        height = float(input("Enter your height: "))
        print(calculator.bmiCalculator(weight, height))
    elif userChoice == "2":
        print("Mode: Lb and Ft")
        weight = float(input("Enter your weight: "))
        poundWeight = weight * 0.453592
        height = float(input("Enter your height: "))
        feetHeight = height * 30.48
        print(calculator.bmiCalculator(poundWeight, feetHeight))
    elif userChoice == "q":
        break
    else:
        print("wrong input, try again")
