import pathlib, shutil

path = pathlib.Path("main.py")
if path.exists():
    shutil.copy2("main.py", f"main1.py")
    print("done")
