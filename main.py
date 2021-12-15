"""
PREFS is a python library to store and manage user preferences.
It stores the settings in a file (usually next to your program) with a simple syntax that you can use to create to create your own files manually.


About:
	Documentation: https://patitotective.github.io/PREFS/docs.
	Website: https://patitotective.github.io/PREFS.
	GitHub: https://github.com/Patitotective/PREFS
	Pypi: https://pypi.org/project/PREFS/.

Contact:
	Discord: Patitotective#0127.
	Twitter: twitter.com/patitotective.
	GitHub: github.com/Patitotective.
	Email: cristobalriaga@gmail.com.
"""

# Libraries
import json
import yaml
import os
import inspect
import types
import warnings
import pkgutil

# Dependencies
from src.utils import check_path, remove_comments, get_built_file_path
from src.prefs import Prefs

__version__ = '0.3.0'
RESOURCE_FILE_HEADER = "# PREFS resource file\n# Created using PREFS Python library\n# https://patitotective.github.io/PREFS/\n# Do not modify this file\n\n"

def check_for_module_resources(modules: list):
	"""Check for module resources in a modules list.
	"""
	result = []

	for module_name, module in modules:
		if not hasattr(module, "__file__"):
			continue

		with open(module.__file__, "r") as file:
			module_content = file.read()

			if not module_content.startswith(RESOURCE_FILE_HEADER):
				continue

			if not hasattr(module, "VERSION") or not hasattr(module, "PREFS") or not hasattr(module, "ALIAS"):
				continue

			if module.VERSION != VERSION:
				warnings.warn(
					f"Resource file has a different version, it can cause some errors.\nCurrent version: {VERSION} Resource file version: {module.VERSION}", 
					DeprecationWarning
				)

		result.append(module)

	return result

def bundle_prefs_file(path: str, output: str=None, alias: str=None):
	if output is None:
		output = f"{path.split('.')[0]}_resource.py"
	if alias is None:
		alias = os.path.basename(path)

	prefs = PrefsBase({}, path).file
	
	check_path(output)

	with open(output, "w+") as file:
		file.write(RESOURCE_FILE_HEADER)
		file.write(f"VERSION = {VERSION!r}\nPREFS = {prefs}\nALIAS = {alias!r}\n")

	print(f"'{output}' resource file created with '{alias}' as alias.")

def read_json_file(filename: str, **kwargs) -> any:
	"""Reads Json files and returns it's value.

	Note:
		Object (dict) expected.

	Args:
		filename (str): The name of the json file to read
		extension (str, optional="json"): The extension of the json file.

	Returns:
		dict
	"""

	with open(filename, "r") as file: # Open json file
		data = json.load(file, **kwargs) # Load json file

	return data # Return data in the json file

def read_yaml_file(filename: str, Loader=yaml.loader.SafeLoader, **kwargs) -> dict:
	"""Reads YAML files and returns it's values.

	None:
		Dict object expected in YAML file.

	Args:
		filename (str): The name of the yaml file to read
		extension (str, optional="yaml"): The extension of the yaml file.

	Returns:
		dict

	"""
	data = {}
	
	with open(filename, "r") as file:
		data = yaml.load(file, Loader=Loader, **kwargs)

	return data 

def read_prefs_file(filename: str, **kwargs) -> dict:
	"""Return the value of Prefs file given it's filename.
	
	Notes:
		`module` variable means the module where Prefs was imported in.
		`modules_inside` variable means the modules inside `module`.	
	
	Returns:
		A dictionary.

	"""
	if filename[:2] == ":/": # Means it's a resource (module or binary)
		"""Check for resources in the given list of modules.

		Notes:
			There are two types of resources, module resources and binary resources:
				- Module resources are stored like another Python module.
				- Binary resources are data stored in a binary file with pyisntaller (or so).
			
			Checks first for module resources, if there are no resources check for binary ones.
		"""
		
		## Check for module resources ###

		# Get the module where this function was called from
		module_frame = inspect.getouterframes(inspect.currentframe())[1].frame # https://stackoverflow.com/a/7151403/15339152
		module = inspect.getmodule(module_frame)
		modules_inside = inspect.getmembers(module, predicate=lambda obj: isinstance(obj, types.ModuleType))
		
		# Check for resources inside the modules inside the module this function was called frm
		resources = check_for_module_resources(modules_inside)
		for resource in resources:
			if filename[2:] == resource.ALIAS: # If the filename (without :/) is the same as the resource alias
				# Return the resource prefs
				return resource.PREFS
		
		# If there is no resources with that alias, raise an error
		raise InvalidResourceAlias(f"Couldn't find {filename!r} alias.")

	built_filename = get_built_file_path(filename) # Will return the build path if there is one otherwise None

	if built_filename is not None:
		if "verbose" in kwargs and kwargs["verbose"]:
			print(f"Found PREFS data at {built_filename} ({filename})")
		
		filename = built_filename

	prefs_instance = PrefsBase(**kwargs)

	return prefs_instance.read_prefs(filename=filename)

def convert_to_prefs(*args, output: str=None, **kwargs) -> (str, None):
	
	"""Given a dictionary convert that dictionary into Prefs format and return it as string. 
	
	Returns:
		A string contating the dictionary in Prefs format.

	"""

	prefs_instance = PrefsBase(*args, filename=None, **kwargs)

	if output is None:
		return prefs_instance.dump()

	check_path(output)

	with open(output, "w+") as file:
		file.write(prefs_instance.dump())

if __name__ == "__main__":
	pass
