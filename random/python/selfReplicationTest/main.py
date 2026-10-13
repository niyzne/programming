import pathlib
import shutil

path = pathlib.Path("main.py")
if path.exists():
    shutil.copy2("main.py", "HelloWorld.py")
    print("done")
