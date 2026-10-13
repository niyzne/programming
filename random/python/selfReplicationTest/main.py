import pathlib
import shutil
from notifypy import Notify
import uuid
import os

def notification():
    notification = Notify()
    notification.title = "Python"
    notification.message = "Hello, World"
    notification.send()

def ownFileName():
    filename = os.path.basename(__file__)
    return filename

def newRandomName():
    filename = str(uuid.uuid4()) + ".py"
    return filename

def dupe():
    path = pathlib.Path("main.py")
    if path.exists():
        shutil.copy2(ownFileName(), newRandomName())
        notification()

def amountOfTimes():
    times = int(input("How many times do you want to dupe: "))
    for i in range(times):
        dupe()

while True:
    userChoice = input("Select an option\n[1] print x amount of random files\n[q] quit\nYour Choice: ")
    if userChoice == "1":
        amountOfTimes()
    elif userChoice == "q":
        print("Goodbye")
        break
    else:
        print("Wrong input")
