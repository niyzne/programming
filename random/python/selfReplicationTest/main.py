import pathlib
import shutil
from notifypy import Notify
import uuid

def notification():
    notification = Notify()
    notification.title = "Python"
    notification.message = "Hello, World"
    notification.send()

def randomName():
    filename = str(uuid.uuid4()) + ".py"
    return filename

def dupe():
    path = pathlib.Path("main.py")
    if path.exists():
        shutil.copy2("main.py", randomName())
        notification()

dupe()
