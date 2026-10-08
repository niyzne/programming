import calculator

while True:
    userChoice = input("Welcome to BMI calculator\n[1] KG and CM\n[2] Lb and Ft\n[q] quit\nYour choice: ")
    if userChoice == "1":
        print("Mode: KG and CM")
        weight = float(input("Enter your weight: "))
        height = float(input("Enter your height: "))
        bmi = calculator.bmiCalculator(weight, height)
        bmi_status = calculator.bmiStatus(bmi)
        print(f"Your BMI is {bmi}")
        print(f"Your BMI status is {bmi_status}")
    elif userChoice == "2":
        print("Mode: Lb and Ft")
        weight = float(input("Enter your weight: "))
        poundWeight = weight * 0.453592
        height = float(input("Enter your height: "))
        feetHeight = height * 30.48
        bmi = calculator.bmiCalculator(poundWeight, feetHeight)
        bmi_status = calculator.bmiStatus(bmi)
        print(f"Your BMI is {bmi}")
        print(f"Your BMI status is {bmi_status}")
    elif userChoice == "q":
        break
    else:
        print("wrong input, try again")
