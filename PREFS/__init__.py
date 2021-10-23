"""
PREFS is a simple but useful python library to store and manage user preferences. PREFS creates a file with your preferences, and allows you to manage these as you like.

Requirements:
	pyyaml

Content:
	PrefsBase (class): This class have all the functions to manage a PREFS file
	Prefs (class): Inherits from PrefsBase, checks if a file exists and read it, otherwise create it.
	check_for_module_resources (function): Given a list of modules check if any of them is a PREFS resource.
	bundle_prefs_file (function): Given the path of a PREFS file generates a resource file.
	read_json_file (function): Simple Reads a json file and returns it's value.
	read_yaml_file (function): Simple Reads a yaml file and returns it's value.
	read_prefs_file (function): Given a filename (and optional other parameters) of a PREFS file return it's value.
	convert_to_prefs (function): Given a dictionary (and option other parameters) return the text of a PREFS file (like json dump function)

This library's source code is hosted at GitHub: https://github.com/Patitotective/PREFS.
Complete documentation at https://patitotective.github.io/PREFS/.
This package is public at https://pypi.org/project/PREFS/.

Made by Patitotective.
Contact me:
	Discord: Patitotective#0127.
	Email: cristobalriaga@gmail.com.
"""

# Libraries
import json # To support export/import json files
import yaml # To support export/import yaml files
import os # To manage paths, folders and files
import ast # To eval code without using eval built-in module
import inspect # To get the module where PREFS was imported from and list all the libraries/modules in a module
import types # To get Python types
import warnings # To warn of differente PREFS resource file versions
import pkgutil # To get binary data in binary files (when it's built with pyinstaller)
from typing import List, Dict # To better document the code
from .extra import check_path, remove_comments, get_built_file_path

VERSION = "v0.2.60"
RESOURCE_FILE_HEADER = "# PREFS resource file\n# Created using PREFS Python library\n# https://patitotective.github.io/PREFS/\n# Do not modify this file\n\n"


class InvalidKeyError(Exception):
	"""This error is raised when a key is not valid.
	"""
	pass


class InvalidResourceAlias(Exception): 
	"""This error will be raised when a PREFS resource is not valid.
	"""
	pass


class DeprecationWarning(Warning):
	"""Overwriting default DeprecationWarning, otherwise warn doesn't work.
	"""
	pass


class PrefsBase: 	
	def __init__(
		self, 
		prefs: dict=None, 
		filename: str="prefs.prefs", 
		verbose: bool=False, 
		auto_generate_keys: bool=True
	):

		self.SEPARATOR_CHAR = "="
		self.ENDER_CHAR = "\n"
		self.CONTINUER_CHAR = ">"
		self.COMMENT_CHAR = "#"
		self.INDENT_CHAR = "\t"

		self.prefs = prefs
		self.filename = filename

		self.verbose = verbose


		self.auto_generate_keys = auto_generate_keys
		
		self.first_line = "#PREFS" # First line of all prefs file to recognize them.

	def check_file(self):
		"""Try to call read_prefs() method and if raises FileNotFoundError calls create_prefs() method.

		Returns:
			None
		"""

		if os.path.isfile(self.filename): # Try to open the file and if it doesn't exist create it
			return self.read_prefs()

		if self.verbose: print(f"File not found. Trying to create {self.filename}")
		self.create_prefs(self.prefs) # Create Prefs file with default prefs dict

	@property
	def file(self):
		return self.read_prefs()

	def read_prefs(self, filename=None) -> dict:
		"""Reads prefs file and returns it's value in a dictionary.
	
		Parameters:
			filename=None: the filename of the prefs file to read, if no specified self.filename.

		Returns:
			A dictionary with all the prefs.
		"""
		if filename is None:
			filename = self.filename

		if self.verbose: print(f"Trying to read {filename}")

		content = {} # Content will be where the prefs will be stored when reading

		with open(filename, "r") as file: # Open the file with read permissions
			lines = file.read().split("\n") # Read lines

			if len(lines) == 0:
				if self.verbose: print(f"Emtpy file {filename}")
				return {}

			content = self.tree_to_dict(lines) # Interpreting the result of get_lines_properties() returns the dictionary with the prefs. 

		if self.verbose: print(f"Read {filename}")

		return content # Return prefs file as dictionary

	def tree_to_dict(self, lines: dict, level: int=0) -> dict:
		"""Given the result of get_lines_properties() returns a dictionary with the prefs.
		Given the list of lines of the prefs file returns a dictionary with 
		each line's properties, such as key, val and indent_level.
		
			Note:
				This code is based on this answer https://stackoverflow.com/questions/17858404/creating-a-tree-deeply-nested-dict-from-an-indented-text-file-in-python/24966533#24966533.

			Args:
				lines (dict): List of dictionaries with lines properties, such as key, val and indent_level.

			Returns:
				A dictionary interpreting lines.
		"""
		def get_line_num(line_num):
			"""Return the right line number.
			"""
			return level + line_num + 1 if level < 1 else level + line_num + 2

		def get_line_info(line: str, raw_line: str, line_num: int):
			indent_level = len(line) - len(line.lstrip(self.INDENT_CHAR)) # Count the indents of the line 

			try:
				key, val = line.strip().split(self.SEPARATOR_CHAR, 1) # Split the line by the default separator only once
				if key == "" or val == "":
					raise SyntaxError(f"Could not read line {get_line_num(line_num)}: \n\t{line.strip()}\nin {self.filename} file (hint: empty key or value)")

			except ValueError:
				raise SyntaxError(f"Could not read line {get_line_num(line_num)}: \n\t{raw_line.strip()}\nin {self.filename} file (hint: missing separator {self.SEPARATOR_CHAR!r})")

			return {"key": key, "val": val, "indent_level": indent_level} # Append the above values in dict format to the result list
				
		def clean_line(line: str) -> list:		
			line = remove_comments(line, comment_char=self.COMMENT_CHAR)
			line = line.rstrip() # To keep left indentations

			return None if line.strip() == "" else line
		
		def eval_val(val: str) -> any:
			def eval_string(string: str) -> any:
				"""Evaluates representation of python types, str, bool, list.
					
					Args:
						string (str): A string to evaluate.

					Returns:
						The string evalueated.
				"""
				if len(string) == 0: return string # If empty string return empty

				elif string == "True": # If string equals True return True
					result = True
				elif string == "False": # If string equals False return False
					result = False
				else: # If none of above types evaluate with eval
					result = ast.literal_eval(string)

				return result
			
			if isinstance(val, dict): # If dictionary type calls itself to evaluate
				return self.eval_dict(val) # Using recursive function to get all values in cascade/tree.
			
			return eval_string(val) # If don't dictionary call eval_string() method.

		result = {}

		for line_num, line in enumerate(lines):
			raw_line = line
			line = clean_line(line)
			
			if line is None: # Means it's emtpy
				continue

			## Get line info ##
			line_info = get_line_info(line, raw_line, line_num)

			if line_info['key'] in result:
				if self.verbose:
					warnings.warn(f"Repeated key {line_info['key']!r} at {get_line_num(line_num)}", SyntaxWarning)

			## Eval value ##
			if line_info["val"] != self.CONTINUER_CHAR:
				try:
					line_info["val"] = eval_val(line_info["val"])
				except (SyntaxError, ValueError):
					raise SyntaxError(f"Could not eval line {get_line_num(line_num)}: \n\t{raw_line.strip()}\nin {self.filename}")

			## Check for indentation errors and next line ##
			if line_num < len(lines) - 1 and not clean_line(lines[line_num + 1]) is None:
				raw_next_line = lines[line_num + 1]
				next_line = clean_line(raw_next_line)
							
				next_line_info = get_line_info(next_line, raw_next_line, line_num + 1)
				if line_info['val'] == self.CONTINUER_CHAR and next_line_info["indent_level"] != line_info["indent_level"] + 1:
					raise IndentationError(f"Expected indent block after line ~{get_line_num(line_num)} (remember to indent with tabulations)")
				
				if next_line_info["indent_level"] == line_info["indent_level"] + 1 and line_info["val"] != self.CONTINUER_CHAR:
					raise IndentationError(f"Unexpected indentation found at line {get_line_num(line_num + 1)}: \n\t{lines[line_num + 1].strip()}\nin {self.filename}")

			else:
				if line_info['val'] == self.CONTINUER_CHAR:
					raise IndentationError(f"Expected indent block after line ~{get_line_num(line_num)} (remember to indent with tabulations)")

				next_line_info = {"indent_level": -1}

			## Edge cases ##
			if line_info['indent_level'] > level:
				continue
			
			if line_info['indent_level'] < level:
				return result

			## Add keys and values ##
			if next_line_info['indent_level'] > level:
				nested_dict = self.tree_to_dict(lines[line_num + 1:], level=next_line_info['indent_level'])
				result[line_info['key']] = nested_dict

			else:
				result[line_info['key']] = line_info['val']
		
		return result

	def dump(self, prefs=None) -> str:
		"""Given a dictionary return it on Prefs format.
		"""
		if prefs is None:
			prefs = self.prefs

		if callable(prefs): # If self.prefs is a function call it
			prefs = prefs() # Setting prefs to self.prefs function returns alue

		if not isinstance(prefs, dict): # If isn't a dict raise error
				raise TypeError(f"self.prefs must be a dictionary or a function with a dictionary as return value, gived {type(prefs).__name__}")

		result = f"{self.first_line}{self.ENDER_CHAR}"
		result += self.dict_to_tree(prefs) # Calls dict_to_tree() method which convert a dictionary into prefs file
		
		return result

	def create_prefs(self, prefs: dict) -> None:
		"""Creates a file with the prefs that you pass.

			Args:
				prefs (dict): The prefs that will write in the file.

			Returns:
				None
		"""
		if callable(prefs): # If self.prefs is a function call it
			prefs = prefs() # Setting prefs to self.prefs function returns alue

		if not isinstance(prefs, dict): # If isn't a dict raise error
				raise TypeError(f"self.prefs must be a dictionary or a function with a dictionary as return value, gived {type(prefs).__name__}")
	
		check_path(self.filename)

		with open(self.filename, "w+") as prefs_file: # Opening the file with all permissions

			if self.verbose: print(f"Creating {self.filename}")

			prefs_file.write(f"{self.first_line}{self.ENDER_CHAR}") # First line will be self.first_line to recognize Prefs files
			
			lines = self.dict_to_tree(prefs) # Calls dict_to_tree() method which convert a dictionary into prefs file
			prefs_file.write(lines) # Writes the result of dict_to_tree() in the prefs file.

			if self.verbose: print(f"{self.filename} created")

		self.check_file() # Read prefs to check the Prefs file and update file attribute 

	def dict_to_tree(self, prefs: dict, depth=0) -> str:
		"""Converts the prefs dictionary to prefs file.

			Args:
				prefs (dict): a dictionary with the prefs to convert to text.
				depth (int=0): This value will multiply "\t" which means a tabulation

			Returns:
				An string with the prefs, ready to write.
		"""	
		if callable(prefs): # If self.prefs is a function call it
			prefs = prefs() # Setting prefs to self.prefs function returns alue

		if not isinstance(prefs, dict): # If isn't a dict raise error
				raise TypeError(f"prefs argument must be a dictionary or a function with a dictionary as return value, gived {type(prefs)}")
		
		result = "" # String to append each pref:value combination
		indent_char = self.INDENT_CHAR * depth # Multiply depth by a tabulation, e.i.: if depth 0 no tabulation.

		for key, val in prefs.items(): # Iterate through prefs dictionary items
			self.check_key(key)

			if isinstance(val, dict) and val != {}: # If values is a dictionary and cascade is True and isn't an empty dictionary
				result += f"{indent_char}{key}{self.SEPARATOR_CHAR}{self.CONTINUER_CHAR}{self.ENDER_CHAR}" # Writes indent_char val and => to indicate that value in the text line.
				result += self.dict_to_tree(val, depth=depth + 1) # Calls itself to generate cascade/tree
				continue

			result += f"{indent_char}{key}{self.SEPARATOR_CHAR}{val!r}{self.ENDER_CHAR}" # Write key:value (str) with quotes

		return result

		self.check_file() # Read prefs to check the Prefs file and update file attribute 

	def check_key(self, key: str) -> None:
		if not isinstance(key, str):
			raise InvalidKeyError(f"Invalid key {key!r}. A key can only be a string, gived {type(key).__name__}")			

		if "/" in key or "=" in key:
			raise InvalidKeyError(f"Invalid key {key!r}. A key cannot include the following characters '/='")

	def write_prefs(self, pref: str, value: any) -> None:
		"""Change the pref that you pass with the value that you pass, if doesn't exist, new pref.
			To change nested dictionary pass path, e.g.: write_prefs(pref="keybindings/Copy", value="ctrl+c")
			
			Args:
				pref (str): the name of the pref that you want to change, if it doesn't exist, it will create it.
				value (any): the value that you want to assign to the pref.

			Returns:
				None

		"""

		if self.verbose: print(f"Trying to write {pref} with {value} value in {self.filename}")
		
		content = self.read_prefs() # Get prefs dictionary

		if "/" in pref: # If / in pref means that prefs is a nested dictionary
			content = self.change_nested_dict_val(content, pref, value) # Calls method that change value of nested dictionaries.
		else: # If not / in pref
			content[pref] = value # Simply change pref to given value


		self.create_prefs(content) # Replace old file with updated file

		if self.verbose: print(f"Writed {pref} with {value} value in {self.filename}")

		self.check_file() # Read prefs to check the Prefs file and update file attribute 

	def write_multiple_prefs(self, prefs: Dict[str, any]) -> None:
		"""Given a list of prefs and a list of values, cahnges all prefs with it's corresponding value (like write_prefs).
		This way is more eficiently that opening and closing a file 10 times.
			
		Args:
			prefs: Dict[str, any]

		Returns:
			None
		"""
		if self.verbose: print(f"Trying to write multiple prefs in {self.filename}")
		
		content = self.read_prefs() # Get prefs dictionary

		for pref, value in prefs.items():
			if "/" in pref: # If / in pref means that prefs is a nested dictionary
				content = self.change_nested_dict_val(content, pref, value) # Calls method that change value of nested dictionaries.
			else: # If not / in pref
				content[pref] = value # Simply change pref to given value

		self.create_prefs(content) # Replace old file with updated file

		if self.verbose: print(f"Wrote multiple prefs in {self.filename}")

		self.check_file() # Read prefs to check the Prefs file and update file attribute 

	def change_nested_dict_val(self, dict_: dict, keys: str, val: any) -> dict:
		"""Iterate through given dictionary until find last key and set that key to the given value.

			Args:
				dict_ (dict): A dictionary to search to/change value.
				keys (str): A "path" to the key. e.g.: "keybindings/Copy".
				val (any): The val to set to the key.

			Returns:
				The given dictionary changing the given key to the given value.
		"""
		keys = keys.split("/") # Split the keys by /
		
		if not keys[0] in dict_:
			dict_[keys[0]] = {}

		scn_dict = dict_[keys[0]] # Set scn_dict to the first key of dict_

		keys.pop(0) # Remove the fist key from the keys list

		for e, i in enumerate(keys): # Iterate through the keys
			if e < len(keys) - 1: # While  key isn't the last
				if not i in scn_dict and self.auto_generate_keys:
					scn_dict[i] = {}

				scn_dict = scn_dict[i] # Set scn_dict to scn_dict key


			else: # If last key
				scn_dict[i] = val # Set key to val
				
		return dict_

	def overwrite_prefs(self, prefs: dict = None) -> None:
		"""Over writes the current prefs with the default prefs, if dictionary passed over write the prefs with these.
			
			Args:
				prefs (dict, optional): New prefs, if empty reset prefs to default ones.

			Returns:
				None  
		"""
		if not os.path.isfile(self.filename):
			raise FileNotFoundError("Cannot overwrite unexistent prefs") # If file isn't in the path raise error

		if prefs is not None: # If prefs isn't none it must be a dictionary
			if not isinstance(prefs, dict):  # If isn't a dict raise error
				raise TypeError(f"prefs must be a dictionary or a function with a dictionary as return value, gived {type(prefs)}")

		if self.verbose: print(f"Trying to overwrite {self.prefs} in {self.filename}")

		self.delete_file() # Delete file to create it again

		if prefs is None:
			self.create_prefs(self.prefs) # Create prefs with default value
		elif isinstance(prefs, dict): # If isn't none is because you have passed an argument so create the new file with the passed prefs
			self.create_prefs(prefs) # Create prefs file with given dictionary

		if self.verbose: print(f"Overwrited {self.prefs} in {self.filename}")

		self.check_file() # Read prefs to check the Prefs file and update file attribute 
			
	def change_filename(self, filename: str) -> None:
		"""Changes the name of the file.
		
		Note:
			The filename will be changed but you have to change it's name at class init, other wise a Prefs file with the old name will be created when you run the program again.

		Args:
			filename (str): the new name of the file.

		Returns:
			None

			"""
		if not os.path.isfile(self.filename): # If file isn't in the path raise error
			raise FileNotFoundError("Cannot change the name of a file that doesn't exists")
		
		if self.verbose: print(f"Trying to change {self.filename} name to {filename}")
		
		os.rename(self.filename, filename) # Rename file with os
		
		self.filename = filename # Change self.filename to passed filename

		if self.verbose: print(f"Changed filename to {self.filename}")

		self.check_file() # Read prefs to check the Prefs file and update file attribute 

	def delete_file(self) -> None:
		"""Deletes the prefs file (if you run your code again it will be created again).

		Returns:
			None

		"""
		if not os.path.isfile(self.filename): # If file is in the path
			raise FileNotFoundError("Can't delete unexistent file") # Raise error because file isn't in the specified path

		if self.verbose: print(f"Trying to remove {self.filename}")
		
		os.remove(self.filename) # Remove file
		
		if self.verbose: print(f"Removed {self.filename}")

	def convert_to_json(self, filename: str=None, **kwargs) -> None:
		"""Converts the prefs file to a json file.
		
		Args:
			filename (str, optional=""): As default the same name as your prefs file but with .json extension.

		Returns:
			None
		"""
		# If don't passed any filename set filename as self.filename, if filename passed set filename as filename 
		if filename is None:
			filename = f"{os.path.splitext(self.filename)[0]}.json"

		if self.verbose: print(f"Trying to dump {filename}")

		with open(filename, "w") as outfile: # Creating new json file
			json.dump(self.file, outfile, **kwargs) # Saving Prefs in json file

		if self.verbose: print(f"Successfuly created {filename}")

	def convert_to_yaml(self, filename: str=None, **kwargs) -> None:
		"""Converts the prefs file into a yaml file.
		
		Args:
			filename (str, optional=""): As default the same name as your prefs file but with .yaml extension.
		Returns:
			None
		"""

		# If don't passed any filename set filename as self.filename, if filename passed set filename as filename 
		if filename is None:
			filename = f"{os.path.splitext(self.filename)[0]}.yaml"

		if self.verbose: print(f"Trying to dump {filename}")

		with open(filename, "w") as outfile: # Creating new yaml file
			yaml.dump(self.file, outfile, **kwargs) # Saving Prefs in yaml file disablig sort_keys and default_flow_style

		if self.verbose: print(f"Successfuly created {filename}")	


class Prefs(PrefsBase): 
	"""Prefs class creates a file to store and manage user preferences.
	
	Attributes:
		file(dict): easier way to get the read_prefs() returns value (to get the prefs).

	Methods:
		check_file() -> None: Try to call read_prefs() and if raises FileNotFoundError call create_prefs(), returns None.

		read_prefs() -> dict: Call get_lines_properties and pass that value to tree_to_dict to get the prefs inside the file. Returns the prefs in a dictionary.

		get_lines_properties(lines: list) -> dict: Given a lines of a prefs file returns a dictionary with each line key, value and indent_level.
		
		tree_to_dict(ttree: dict, level: int=0) -> dict: Given the result of get_lines_properties() interprets the indent_level and returns a dictionary with the prefs.

		create_prefs(prefs: dict) -> None: Creates a file with the given prefs and the 
		Prefs class filename, returns None.

		write_prefs(pref: str, value: any) -> None: Reading the prefs file as a dictionary 
		changes the passed pref to the passed value, if the pref (key) doesn't exist it 
		creates it. If using nested dictionaries calls change_nested_dict_val() to change the given pref to the given value, returns None.

		change_nested_dict_val(myDict: dict, keys: str, val: any) -> dict: Given a dictionary, a keys separeted by / and a value, search through the dictionary the keys and set the value, returns the dictionary with the changed value.

		overwrite_prefs(prefs: dict=None) -> None: Over writes the current prefs file 
		with the default prefs or if given a dictionary over writes the prefs file with it, returns None.

		change_filename(filename: str) -> None: Changes the name of the prefs file 
		with the given one, returns None.

		delete_file() -> None: Removes the file if it exists, returns None.

		convert_to_json(self, filename: str="") -> None: Creates a json file with the actual prefs, if filename don't passed the prefs filename will be the json filename, returns None.
	
		convert_to_yaml(self, filename: str="") -> None: Creates a yaml file with the actual prefs, if filename don't passed the prefs filename will be the yaml filename, returns None.
	"""
		
	def __init__(self, prefs: dict, *args, **kwargs):
		
		"""	
		Args
			prefs (dict): A dictionary with the default preferences.
			filename (str, optional="prefs"): The name of the file (supports path).
			interpret (bool, optional=True): Interpret the value stored as python.
			verbose (bool, optional=False): Print logs all operations.
			cascade (bool, optional=True): Stores nested dictionaries as tree/cascade.
			indent_char (str, optional="\t"): The character to indent_char with.
			comment (str, optional="#"): Character to indicate comments (all text after them and outside quotes will be ignored) 
			auto_generate_keys (bool, optional=True): When using write_prefs if nested path doesn't exist create it.
		"""
		
		super().__init__(prefs, *args, **kwargs)

		self.check_file()
		

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
