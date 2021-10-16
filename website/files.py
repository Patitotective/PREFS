# Libraries
import glob
import os
from os import path as ospath
import shutil
import time

# import frontmatter
# from pathlib import Path

# getDirs = lambda dirname: [f.path for f in os.scandir(dirname) if f.is_dir()]

# directories = [i.replace("./", "") for i in getDirs(".")]

"""
def AddVersion(directories, extension="md"):
	for folder in directories:
		
		files = glob.glob(f"{folder}/*.{extension}")

		for filename in files:
			if "versions" in filename: continue
			
			file = frontmatter.load(filename)
			
			permlink = file.metadata["permalink"]
			permlink = permlink.split("/")
			permlink[0] = folder

			file["version"] = folder

			permlink = "/".join(permlink)
			
			file["permalink"] = permlink
			frontmatter.dump(file, filename)
"""

def copy_file(path: str, new_path: str, prefix: str="", suffix: str=""):

	if os.path.exists(new_path): os.remove(new_path)

	with open(new_path, "w+") as new_file:
		with open(path) as file:
			content = file.read()

			new_file.write(prefix)
			new_file.write(content)
			new_file.write(suffix)

def copy_folder(path: str, new_path: str):
	if ospath.isdir(new_path): 
		print(f"{new_path} is going to be replaced with {path}")
		time.sleep(1)
		
		shutil.rmtree(new_path)

	shutil.copytree(path, new_path)


if __name__ == "__main__":
	copy_file(
		path="/home/cristobal/Documents/Projects/PREFS/Code/docs/CHANGELOG.md", 
		new_path="docs/about/CHANGELOG.md", 
		prefix="---\nid: changelog\ntitle: Change log\nhide_title: true\nsidebar_position: 5\n---\n")
		
	print("Successfully completed")
