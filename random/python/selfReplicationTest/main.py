import pathlib
import shutil
import uuid
import os
import subprocess

colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "reset": "\033[0m"
}

def invalidInput():
    print(f'{colors["red"]}Invalid input, try again{colors["reset"]}')

def goodbye():
    print(f'{colors["blue"]}Have a good day{colors["reset"]}')

def notification():
    subprocess.run([
        "notify-send",
        "-a", " ",
        "Hello, World",
    ])

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
    userChoice = input("Select an option\n[1] make x amount of files\n[q] quit\nYour Choice: ")
    if userChoice == "1":
        print(f'{colors["yellow"]}Mode selected: make x amount of files{colors["reset"]}')
        amountOfTimes()
    elif userChoice == "q":
        goodbye()
        break
    else:
        invalidInput()
