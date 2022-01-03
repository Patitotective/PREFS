"""
PREFS is a Python library to store and manage preferences or settings.
Preferences are stored as dictionaries in a text file with an special and simple syntax.

Notes:
	Resources:
		- Module resources are refered to PREFS files converted into Python modules (see https://patitotective.github.io/PREFS/docs/resources)
		- Binary resources are data stored in a binary file with PyInstaller.
		Checks first for module resources, if there are no resources check for binary ones.

About:
	Documentation: https://patitotective.github.io/PREFS/docs.
	Website: https://patitotective.github.io/PREFS.
	GitHub: https://github.com/Patitotective/PREFS.
	Pypi: https://pypi.org/project/PREFS.

Contact:
	Discord: Patitotective#0127.
	Twitter: twitter.com/patitotective.
	GitHub: github.com/Patitotective.
	Email: cristobalriaga@gmail.com.
"""
import os
import types
import inspect
import warnings

from .parser import parser
from .prefs import PrefsBase, Prefs
from .exceptions import DeprecationWarning
from .exceptions import InvalidResourceError
from .utils import check_path, get_built_file_path, load_module_from_path


__version__ = '1.0.1'
RESOURCE_FILE_HEADER = """# PREFS resource module
# Created using PREFS Python library
# https://patitotective.github.io/PREFS
# Do not modify this file
"""

def is_resource_module(module: types.ModuleType) -> bool:
	if not hasattr(module, "__file__"): # Meaning is a built-in
		return False

	if not hasattr(module, "__version__") or not hasattr(module, "CONTENT") or not hasattr(module, "ALIAS"):
		return False

	if module.__version__ != __version__:
		warnings.warn(
			f"The current PREFS version differs from {module.ALIAS} resource module one, some errors may occur.\nCurrent version: {__version__}\n{module.ALIAS} version: {module.__version__}",
			DeprecationWarning # Imported DeprecationWarning
		)

	return True

def bundle(path: str, output: str=None, alias: str=None) -> None:
	if output is None:
		output = f"{os.path.splitext(path)[0]}_resource.py"
	if alias is None:
		alias = os.path.basename(path)

	path = os.path.join(os.getcwd(), path)
	content = read(path)
	
	check_path(output)

	with open(output, "w+") as file:
		file.write(RESOURCE_FILE_HEADER)
		file.write(f"__version__ = {__version__!r}\nCONTENT = {content}\nALIAS = {alias!r}\n")

	print(f"'{output}' resource module created with '{alias}' as alias.")

def to_prefs(content: dict, output: str=None) -> str:
	"""Given a dictionary convert that dictionary into Prefs format and return it as string. 
	
	Args:
		content (dict): Prefs content.
		output (str=None): An output path.
	"""

	my_prefs = PrefsBase(content)
	result = my_prefs.to_prefs()

	if output is None:
		return result

	check_path(output)

	with open(output, "w+") as file:
		file.write(result)

	return result

def parse(string: str) -> dict:
	return parser.parse(string=string)

def read(path: str) -> dict:
	"""Return the content of a PREFS file or a Python module given it's path.
	"""
	if os.path.splitext(path)[1] == ".py": # Python resource module
		module = load_module_from_path(path)

		if not is_resource_module(module):
			raise InvalidResourceError(f"{path} file doesn't seem to be a PREFS resource.")

		return module.CONTENT

	elif path[:2] == ":/": # Resource module
		stack = inspect.stack(0)[1] # https://stackoverflow.com/a/7151403/15339152
		module = inspect.getmodule(stack.frame) # Module where prefs was imported in
		modules_inside = inspect.getmembers( # Modules inside `module`.
			module, 
			predicate=lambda obj: isinstance(obj, types.ModuleType)
		)

		resources = filter(lambda x: is_resource_module(x[1]), modules_inside)

		# resource_name, resource
		for _, resource in resources:
			if path[2:] == resource.ALIAS: # If the path (without :/) is the same as the resource alias
				return resource.CONTENT
		
		raise InvalidResourceError(f"Couldn't find any resource module with {path[2:]!r} alias. Make sure to import it at the top and that the versions are compatible.")

	# Will return the binary resource path if there is one otherwise the given one
	path = get_built_file_path(path)

	with open(path, "r") as file:
		return parse(file.read())
