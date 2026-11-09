# starting with something simple

def intToBin(a):
    newNum = ""

    while a > 0:
        num = a % 2
        newNum = str(num) + newNum
        a = a // 2

    return newNum

intNum = int(input("Enter a number: "))
print(intToBin(intNum))
