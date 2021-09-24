"""
PREFS is a simple but useful python library to store and manage user preferences. PREFS creates a file with your preferences, and allows you to manage these as you like.

Requirements:
	pyyaml

Content:
	PREFSBase(class): This class have all the functions to manage a PREFS file
	PREFS (class): Inherits from PREFSBase, checks if a file exists and reade it, otherwise create it.
	read_json_file(function): Simple Reads a json file and returns it's value.
	read_yaml_file(function): Simple Reads a yaml file and returns it's value.
	read_prefs_file (function): Given a filename (and optional other parameters) of a PREFS file return it's value.
	convert_to_prefs(function): Given a dictionary (and option other parameters) return the text of a PREFS file (like json dump function)

This library's source code is hosted at GitHub: https://github.com/Patitotective/PREFS.
Complete documentation at https://patitotective.github.io/PREFS/.
This package is public at https://pypi.org/project/PREFS/.

Made by Patitotective.
Contact me:
	Discord: patitotective#0127.
	Mail: cristobalriaga@gmail.com.
"""

#Libraries
import json # To support export/import json files
import yaml # To support export/import yaml files
import os # To manage paths, folders and files
import ast # To eval code without using eval built-in module
from typing import List # To specify arguments types

VERSION = "0.2.50"

class PREFSBase: 	
	def __init__(self, prefs: dict, filename: str="prefs.prefs", 
		interpret: bool=True, verbose: bool=False, cascade: bool=True, indent_char: str="\t", auto_generate_keys: bool=True):
		
		super().__init__()

		self.prefs = prefs
		self.filename = filename

		self.separator_char = "="
		self.ender_char = "\n"
		self.continuer_char = ">"
		self.comment_char = "#"

		self.interpret = interpret
		self.verbose = verbose
		self.cascade = cascade

		self.indent_char = indent_char

		self.auto_generate_keys = auto_generate_keys
		
		self.first_line = f"#PREFS{self.ender_char}" # First line of all prefs file to recognize it.

	def check_file(self):
		"""
			Try to call read_prefs() method and if raises FileNotFoundError calls create_prefs() method.

			Returns:
				None
		"""

		if os.path.isfile(self.filename): # Try to open the file and if it doesn't exist create it
			return self.read_prefs()

		else:
			if self.verbose: print(f"File not found. Trying to create {self.filename}")
			self.create_prefs(self.prefs) # Create PREFS file with default prefs dict

	@property
	def file(self):
		return self.read_prefs()
	
	def read_prefs(self) -> dict:
		"""Reads prefs file and returns it's value in a dictionary.

			Returns:
				A dictionary with all the prefs.
		"""

		if self.verbose: print(f"Trying to read {self.filename}")

		with open(self.filename, "r") as prefs_file: # Open the file with read permissions
			content = {} # Content will be where the prefs will be stored when reading
			lines = prefs_file.readlines() # Read lines

			content = self.get_lines_properties(lines) # Get lines properties (key, val, indentLevel)
			content = self.tree_to_dict(content) # Interpreting the result of get_lines_properties() returns the dictionary with the prefs. 

			if self.interpret:
				content = self.eval_dict(content) # Pass content to eval_dict function that eval each value.

		if self.verbose: print(f"Read {self.filename}")

		return content # Return prefs file as dictionary

	# The below code is from https://stackoverflow.com/questions/17858404/creating-a-tree-deeply-nested-dict-from-an-indented-text-file-in-python/24966533#24966533
	def get_lines_properties(self, lines: list) -> dict:
		"""Given the list of lines of the prefs file returns a dictionary with 
			each line's properties, such as key, val and indentLevel.
		
			Note:
				This code is based on this answer https://stackoverflow.com/questions/17858404/creating-a-tree-deeply-nested-dict-from-an-indented-text-file-in-python/24966533#24966533.

			Args:
				lines (list): The list of the prefs file lines.

			Returns:
				A list of dictionaries, each dictionary contains the line's properties, such as key (pref). the pref's value and the indentLevel (representing nested dictionaries).
		"""

		result = []

		if len(lines) < 1: raise TypeError("Cannot read the file, it could be empty")
		if lines[0] != self.first_line: raise TypeError("Cannot read the file, it could be corrupted ('#PREFS' must be the first line)")

		for e, line in enumerate(lines): # Iterate through the lines (of the file)

			line = remove_comments(line, comment_char=self.comment_char)
			if not line.strip(): continue # If line emtpy continue

			indentLevel = len(line) - len(line.lstrip(self.indent_char)) # Count the indents of the line 
			keyVal = line.strip().split(self.separator_char, 1) # Split the line by the default separator only once
			try:
				result.append({"key": keyVal[0], "val": keyVal[1], "indentLevel": indentLevel}) # Append the above values in dict format to the result list
			except IndexError:
				raise IndexError(f"Couldn't read line {e} '{line.strip()} in {self.filename}'")

		return result

	def tree_to_dict(self, ttree: dict, level: int=0) -> dict:
		"""Given the result of get_lines_properties() returns a dictionary with the prefs.

			Note:
				This code is based on this answer https://stackoverflow.com/questions/17858404/creating-a-tree-deeply-nested-dict-from-an-indented-text-file-in-python/24966533#24966533.

			Args:
				ttree (dict): List of dictionaries with lines properties, such as key, val and indentLevel.

			Returns:
				A dictionary interpreting ttree.
		"""
		result = {}
		
		for i, cn in enumerate(ttree):
			cn = ttree[i]
			
			try:
				nn  = ttree[i + 1]
			except:
				nn = {'indentLevel': -1}

			# Edge cases
			if cn['indentLevel'] > level:
				continue
			
			if cn['indentLevel'] < level:
				return result

			# Recursion
			if nn['indentLevel'] == level:
				self.dict_instert_append(result, cn['key'], cn['val'])
			
			elif nn['indentLevel'] > level:
				rr = self.tree_to_dict(ttree[i + 1:], level=nn['indentLevel'])
				self.dict_instert_append(result, cn['key'], rr)

			else:    
				self.dict_instert_append(result, cn['key'], cn['val'])
		
				return result
		
		return result

	def dict_instert_append(self, adict: dict, key: str, val: any):
		"""Insert a value in dict at key if one does not exist
			Otherwise, convert value to list and append
		
			Note:
				This code is based on this answer https://stackoverflow.com/questions/17858404/creating-a-tree-deeply-nested-dict-from-an-indented-text-file-in-python/24966533#24966533.
			
			Args:
				adict (dict): A dictionary to insert or append info.
				key (str): The key to insert of append.
				val (any): The values to insert of append to the key.
		"""
		
		if key in adict:
			if not isinstance(adict[key], list):
				adict[key] = [adict[key]]

			adict[key].append(val)
		else:
			adict[key] = val
	
	# The above code is from https://stackoverflow.com/questions/17858404/creating-a-tree-deeply-nested-dict-from-an-indented-text-file-in-python/24966533#24966533

	def dump(self, prefs: dict=None) -> str:
		"""Given a dictionary return it on PREFS format.
		"""

		if prefs is None:
			prefs = self.prefs

		if callable(prefs): # If self.prefs is a function call it
			prefs = prefs() # Setting prefs to self.prefs function returns alue

		if not isinstance(prefs, dict): # If isn't a dict raise error
				raise TypeError(f"self.prefs must be a dictionary or a function with a dictionary as return value, gived {type(prefs).__name__}")

		result = self.first_line
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
	
		if not os.path.isdir(os.path.split(self.filename)[0]) and os.sep in self.filename: # Check if the path to the self.filename exists, if it doesn't create it and if there is a slash on the filename
			directories_list = split_path(os.path.split(self.filename)[0]) # Get all directories to the file
			directories_list = accumulate_list(directories_list, separator=os.sep) # Accumulate them ["home", "cristobal"] -> ["home", "home/cristobal"]
			
			for directory in directories_list: # Iterate trough each directory on the path
				if not os.path.isdir(directory): # If the directory doesn't exist
					os.mkdir(directory) # Create it

		with open(self.filename, "w+") as prefs_file: # Opening the file with all permissions

			if self.verbose: print(f"Creating {self.filename}")

			prefs_file.write(self.first_line) # First line will be self.first_line to recognize PREFS files
			
			lines = self.dict_to_tree(prefs) # Calls dict_to_tree() method which convert a dictionary into prefs file
			prefs_file.write(lines) # Writes the result of dict_to_tree() in the prefs file.

			if self.verbose: print(f"{self.filename} created")

		self.check_file() # Read prefs to check the PREFS file and update file attribute 

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
		indent_char = self.indent_char * depth # Multiply depth by a tabulation, e.i.: if depth 0 no tabulation.

		for key, val in prefs.items(): # Iterate through prefs dictionary items
			
			if isinstance(val, str) and self.interpret: # If value is a string and self.interpret write value with quotes
				result += f"{indent_char}{key}{self.separator_char}{repr(val)}{self.ender_char}" # Write key:value (str) with quotes

			elif isinstance(val, dict) and val != {} and self.cascade: # If values is a dictionary and cascade is True and isn't an empty dictionary

				result += f"{indent_char}{key}{self.separator_char}{self.continuer_char}{self.ender_char}" # Writes indent_char val and => to indicate that value in the text line.
				result += self.dict_to_tree(val, depth=depth + 1) # Calls itself to generate cascade/tree

			else: # If not self.interpret (and key isn't a string) write without quotes
				result += f"{indent_char}{key}{self.separator_char}{val}{self.ender_char}" # Write key:value in file

		return result

		self.check_file() # Read prefs to check the PREFS file and update file attribute 

	def eval_dict(self, prefs: dict) -> dict:
		"""Evaluate dict with strings representing python types (using eval_string() method).

			Args:
				prefs (dict): A dictionary to evalueta and iterate through.

			Returns:
				The same dictionary with all values intrepreted.
		"""
		if not self.interpret:
			return

		result = {}

		for e, (key, val) in enumerate(prefs.items()): # Iterate through prefs dictionary
		
			if isinstance(val, dict): # If dictionary type calls itself to evaluate
				result[key] = self.eval_dict(val) # Using recursive function to get all values in cascade/tree.
				continue

			try:
				result[key] = self.eval_string(val) # If don't dictionary call eval_string() method.
			except SyntaxError as error:
				raise SyntaxError(f"Couldn't eval line {e} in {self.filename}: '{val}'\n{error}")

		return result

	def eval_string(self, string: str) -> any:
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

		self.check_file() # Read prefs to check the PREFS file and update file attribute 

	def write_multiple_prefs(self, prefs: List[str], values: List[any]) -> None:
		"""Given a list of prefs and a list of values, cahnges all prefs with it's corresponding value (like write_prefs).
		This way is more eficiently that opening and closing a file 10 times.
			
			Args:
				prefs (List[str]): a list with the name of the prefs that you want to change, if it doesn't exist, it will create it.
				values (List[any]): a lis with tthe values that you want to assign to each pref in the list respectly.

			Returns:
				None

		"""

		if len(prefs) != len(values):
			raise TypeError("prefs list's length doesn't correspond with values list's length")

		if self.verbose: print(f"Trying to write {prefs} with {values} values in {self.filename}")
		
		content = self.read_prefs() # Get prefs dictionary

		for pref, value in zip(prefs, values):
			if "/" in pref: # If / in pref means that prefs is a nested dictionary
				content = self.change_nested_dict_val(content, pref, value) # Calls method that change value of nested dictionaries.
			else: # If not / in pref
				content[pref] = value # Simply change pref to given value


		self.create_prefs(content) # Replace old file with updated file

		if self.verbose: print(f"Writed {pref} with {value} value in {self.filename}")

		self.check_file() # Read prefs to check the PREFS file and update file attribute 

	def change_nested_dict_val(self, myDict: dict, keys: str, val: any) -> dict:
		"""Iterate through given dictionary until find last key and set that key to the given value.

			Args:
				myDict (dict): A dictionary to search to/change value.
				keys (str): A "path" to the key. e.g.: "keybindings/Copy".
				val (any): The val to set to the key.

			Returns:
				The given dictionary changing the given key to the given value.
		"""
		keys = keys.split("/") # Split the keys by /
		scnDict = myDict[keys[0]] # Set scnDict to the first key of myDict
		keys.pop(0) # Remove the fist key from the keys list

		for e, i in enumerate(keys): # Iterate through the keys
			if e < len(keys) - 1: # While  key isn't the last
				if not i in scnDict and self.auto_generate_keys:
					scnDict[i] = {}

				scnDict = scnDict[i] # Set scnDict to scnDict key


			else: # If last key
				scnDict[i] = val # Set key to val
				
		return myDict

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

		self.check_file() # Read prefs to check the PREFS file and update file attribute 
			
	def change_filename(self, filename: str) -> None:
		"""Changes the name of the file.
		
		Note:
			The filename will be changed but you have to change it's name at class init, other wise a PREFS file with the old name will be created when you run the program again.

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

		self.check_file() # Read prefs to check the PREFS file and update file attribute 

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
			json.dump(self.file, outfile, **kwargs) # Saving PREFS in json file

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
			yaml.dump(self.file, outfile, **kwargs) # Saving PREFS in yaml file disablig sort_keys and default_flow_style

		if self.verbose: print(f"Successfuly created {filename}")	


class PREFS(PREFSBase): 
	"""PREFS class creates a file to store and manage user preferences.
	
	Attributes:
		file(dict): easier way to get the read_prefs() returns value (to get the prefs).

	Methods:
		check_file() -> None: Try to call read_prefs() and if raises FileNotFoundError call create_prefs(), returns None.

		read_prefs() -> dict: Call get_lines_properties and pass that value to tree_to_dict to get the prefs inside the file. Returns the prefs in a dictionary.

		get_lines_properties(lines: list) -> dict: Given a lines of a prefs file returns a dictionary with each line key, value and indentLevel.
		
		tree_to_dict(ttree: dict, level: int=0) -> dict: Given the result of get_lines_properties() interprets the indentLevel and returns a dictionary with the prefs.

		create_prefs(prefs: dict) -> None: Creates a file with the given prefs and the 
		PREFS class filename, returns None.

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
		
	def __init__(self, *args, **kwargs):
		
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
		
		super().__init__(*args, **kwargs)

		self.check_file()
		

def split_path(path: str) -> list:
	result = os.path.normpath(path)
	return path.split(os.sep)

def accumulate_list(my_list: (list, tuple), separator: str="") -> list:
	"""["a", "b", "c"] -> ["a", "ab", "abc"]
	"""
	result = []
	
	for e, ele in enumerate(my_list):
		if e == 0:
			result.append(ele)
			continue

		result.append(f"{result[e-1]}{separator}{ele}")

	return result

def remove_comments(string: str, comment_char: str="#") -> str:
	"""Remove comments from strings.

	Note:
		Iterates through the given string, if founds a quote and there isn't a backslash \ before it set in_string to True, if finds a # and in_string is False break the loop and cut the string until there and return it.
	Args:
		string (str): An string to remove the comments from
		comment_char: (str, optional="#"): Which character represents a comment

	Returns:
		The same string without comments.

	"""

	in_string = False # If iterating in string ignore comments otherwise don't 
	quote = "" # Type of quote (simple or double), because you can't open a string with simple quotes and close it with double

	for e, char in enumerate(string): # Iterate thorught the string
		if char == "'" or char == '"': # Checks if the current character is a quote
			if e != 0: # Checks if the quote isn't in the first place
				if string[e -1] == "\\": # Checks if the character before it is a backslahs
					continue # If it is ignore it

			if quote == char or not in_string: # If the type of quote is the current char, or if isn't in a string
				quote = char # Set the quote to the char
				in_string =  not in_string # And set in_string to True if False and viceversa

		if char == comment_char and not in_string: # If the current character is the comment character and isn't in a string
			string = string[:e] # Cut string until here
			break # And break

	return string # Return the string

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
	
	"""Return the value of PREFS file given it's filename.
		
	Args
		filename (str, optional="prefs"): The name of the file (supports path).
		extension (str, optinal="prefs"): The extension of the file.
		separator (str, optional="="): The character between pref and value in the file.
		ender (str, optional="\n"): The character at the end of each pref:value.
		continuer (str, optional=">"): The character that precede a tree/cascade (nested dictionary).
		interpret (bool, optional=True): Interpret the value stored as python.
		dictionary (bool, optional=False): Writes the prefs as a python dictionary, no more human-readable (avoid any error at reading).
		verbose (bool, optional=False): Pirnt logs all operations.
		cascade (bool, optional=True): Stores nested dictionaries as tree/cascade.
	
	Returns:
		A dictionary reading the PREFS file.

	"""

	prefs_instance = PREFSBase(prefs={}, filename=filename, **kwargs)

	return prefs_instance.read_prefs()

def convert_to_prefs(*args, **kwargs) -> str:
	
	"""Given a dictionary convert that dictionary into PREFS format and return it as string. 
	
	Returns:
		A string contating the dictionary in PREFS format.

	"""

	prefs_instance = PREFSBase(*args, **kwargs)

	return prefs_instance.dump()
