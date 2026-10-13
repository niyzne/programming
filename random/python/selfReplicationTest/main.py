import pathlib
import shutil
from notifypy import Notify

def notification():
    notification = Notify()
    notification.title = "Python"
    notification.message = "Hello, World"
    notification.send()

def dupe():
    path = pathlib.Path("main.py")
    if path.exists():
        shutil.copy2("main.py", f"main1.py")
        notification()

dupe()
