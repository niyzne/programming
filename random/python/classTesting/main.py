import classTest

def callComputer():
    print("You've selected to make a computer")
    computerName = input("Input computer name: ")
    while True:
        computerPrice = input("Input computer price: ")
        if computerPrice.isnumeric():
            computerPrice = int(computerPrice)
            break
        print("Invalid input, try again")
    computerCompany = input("Input computer Company name: ")
    myComputer = classTest.computers(
        computerName, computerPrice, computerCompany
    )

    print(myComputer.name)
    print(myComputer.price)
    print(myComputer.company)
    print(myComputer.nameMessage())
    print(myComputer.priceMessage())
    print(myComputer.companyMessage())

while True:
    userChoice = input("What do you want to do?\n[1] Make Computer\n[q] quit\nYour Choice: ")
    if userChoice == "1":
        callComputer()
    elif userChoice == "q":
        print("Have a good one!")
        break
    else:
        Print("Incorrect statement, try again")
