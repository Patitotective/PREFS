# Libraries
import os
import sys
from importlib.util import spec_from_file_location, module_from_spec


def check_path(path: str):
	"""Check if a path exists, if some directory is missing it creates it.
	"""
	if os.path.exists(path):
		return

	dir_list = split_path(os.path.split(path)[0]) # Remove the filename if there is one and split the directories
	path = dir_list[0]

	for e, dir_ in enumerate(dir_list):
		if os.path.ismount(dir_): # On Windows C:\ and / on Linux
			continue

		if e > 0:
			path = os.path.join(path, dir_) # os.path.join("trial", "sub") -> "trial/sub" (on Windows "trial\sub")

		if not os.path.isdir(path):
			os.mkdir(path)

def split_path(path: str):
	path = os.path.normpath(path) # Remove redundant separators (A//B, A/B/, A/./B and A/foo/../B become A/B)
	# path = os.path.normcase(path) # https://docs.python.org/3/library/os.path.html#os.path.normcase
	path = os.path.expanduser(path) # Convert "~" into the home user directory
	path = path.split(os.sep)
	
	if path[0] == "": # For unix systems
		path[0] = "/" # Add mount point if it got removed when spliting the path
	elif path[0].lower() == "c:":
		path[0] = "C:\\"

	return path

def get_built_file_path(path: str) -> str:
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    bundle_path = os.path.abspath(os.path.join(bundle_dir, path))			

    normal_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), path))

    return bundle_path if bundle_path != normal_path else normal_path

def change_nested_key(dict_: dict, key_path: str, val: any, auto_gen_keys: bool=True, key_path_sep: str="/") -> dict:
	"""Change a nested key with the given key path to the given value.

		Args:
			dict_ (dict): The dictionary to change.
			key_path (str): The path to the key, e.g.: "keybindings/Copy".
			val (any): The val to assign to the key.
	"""
	key_path = key_path.split(key_path_sep)
	
	if not key_path[0] in dict_ and auto_gen_keys:
		dict_[key_path[0]] = {}

	scn_dict = dict_[key_path[0]] # Set scn_dict to the first key of dict_

	key_path.pop(0)

	for e, i in enumerate(key_path):
		if e == len(key_path) - 1:
			scn_dict[i] = val
			continue

		if not i in scn_dict and auto_gen_keys:
			scn_dict[i] = {}

		scn_dict = scn_dict[i] # Set scn_dict to scn_dict key
	
	return dict_

def load_module_from_path(path: str):
	"""Given a path of a Python module, returns it. If some exception when executing the module returns None, error
	"""

	filename = os.path.basename(path) # filename means only the filename without the path, e.g.: PyAPIReference/PyAPIReference/main.py -> main.py
	filename_without_ext = os.path.splitext(filename)[0]

	spec = spec_from_file_location(filename_without_ext, path)
	module = module_from_spec(spec)
	spec.loader.exec_module(module)

	return module
