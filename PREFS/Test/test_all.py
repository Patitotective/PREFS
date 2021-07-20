import subprocess
import glob
import os

files = glob.glob("*.py")
files.remove(os.path.basename(__file__))
[files.remove(i) for i in files if not i.split("_")[0] == "test"]

for file in files:
	subprocess.run(["python3", file])

