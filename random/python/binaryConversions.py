# starting with something simple

def intToBin(a):
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

intNum = int(input("Enter a Number: "))
print(intToBin(intNum))
binNum = int(input("Enter a Binary Number: "))
print(binToInt(binNum))
