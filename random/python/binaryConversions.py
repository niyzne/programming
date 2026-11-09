# starting with something simple

def intToBin(a):
    if a == 0:
        return 0
    else:
        newNum = ""

        while a > 0:
            num = a % 2
            newNum = str(num) + newNum
            a = a // 2

        return newNum

def binToInt(a):
    binSplit = list(str(a))

    pos = 0
    newNum = 0

    for i in reversed(binSplit):
        if i == "1":
            num = 2 ** pos
            newNum += num
            pos += 1
        else:
            pos += 1

    return newNum

while True:
    userInput = input("What do you want to do?\n[1] Convert Intiger to Binary\n[2] Convert Binary to Intiger\n[q] Quit\nYour Choice: ")
    if userInput == "1":
        intNum = input("Enter a Number: ")
        if intNum.isnumeric():
            intNum = int(intNum)
            print(intToBin(intNum))
        else:
            print("Wrong input, Try again")
    elif userInput == "2":
        binNum = input("Enter a Binary Number: ")
        print(binToInt(binNum))
    elif userInput == "q":
        break
    else:
        print("Wrong input, Try again")
