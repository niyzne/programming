import pathlib, shutil
from notifypy import Notify

path = pathlib.Path("main.py")
if path.exists():
    shutil.copy2("main.py", f"main1.py")

    notification = Notify()
    notification.title = "Python"
    notification.message = "Hello, World"
    notification.send()
