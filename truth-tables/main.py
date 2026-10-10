import truthTables

while True:
    userChoice = input("Which truth table would you want to check?\n[1] yes\n[2] not\n[3] and\n[4] or\n[5] nand\n[6] nor\n[7] xor\n[8] xnor\n[q] quit\nYour choice: ")
    if userChoice == "1":
        mode = "yes"
        print(f"Mode selected: {mode}")
        value = int(input("Input 1 or 0: "))
        newValue = truthTables.yesFunction(value)
        print(f"In {mode} mode, the value {value} became {newValue}")
    # elif userChoice == "2":
    # elif userChoice == "3":
    # elif userChoice == "4":
    # elif userChoice == "5":
    # elif userChoice == "6":
    # elif userChoice == "7":
    # elif userChoice == "8":
    elif userChoice == "q":
        break
    else:
        print("wrong input, try again")


# def yesFunction(a):
#   if a == 1:
#     return 1
#   return 0
#
# def notFunction(a):
#   if a == 1:
#     return 0
#   return 1
#
# def andFunction(a, b):
#   if a and b:
#     return 1
#   return 0
#
# def orFunction(a, b):
#   if a or b:
#     return 1
#   return 0
#
# def nandFunction(a, b):
#   if a and b:
#     return 0
#   return 1
#
# def norFunction(a, b):
#   if a or b:
#     return 0
#   return 1
#
# def xorFunction(a, b):
#   if (a or b) and not ((a and b) or (not a and not b)):
#     return 1
#   return 0
#
# def xnorFunction(a, b):
#   if not ((a or b) and not ((a and b) or (not a and not b))):
#     return 1
#   return 0
