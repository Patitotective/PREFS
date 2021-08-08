"""
PREFS is a simple but useful python library to store and manage user preferences. PREFS creates a file with your preferences, and allows you to manage these as you like.

Requirements:
	pyyaml

Content:
	PREFS_Base(class): This class have all the functions to manage a PREFS file
	PREFS (class): Inherits from PREFS_Base, checks if a file exists and reade it, otherwise create it.
	read_json_file(function): Simple Reads a json file and returns it's value.
	read_yaml_file(function): Simple Reads a yaml file and returns it's value.
	read_prefs_file (function): Given a filename (and optional other parameters) of a PREFS file return it's value.
	convert_to_prefs(function): Given a dictionary (and option other parameters) return the text of a PREFS file (like json dump function)

This library's code is hosted in GitHub: https://github.com/Patitotective/PREFS.
Complete documentation in https://patitotective.github.io/PREFS/.
This package is public in https://pypi.org/project/PREFS/.

Made py Patitotective.
Contact me:
	Discord: patitotective#0127
	Mail: cristobalriaga@gmail.com
"""

#Libraries
import json # To support export/import json files
import yaml # To support export/import yaml files
import os # To manage paths, folders and files
from os import path # To check if file or folder exists in path
import sys
import warnings # To send warnings

class PREFS_Base: 
		
	def __init__(self, prefs: dict, filename: str="prefs", extension: str="prefs", separator: str="=", ender: str="\n", continuer: str=">", 
		interpret: bool=True, dictionary: bool=False, verbose: bool=False, cascade: bool=True, indent: str="\t", comment: str="#"):
		
		super(PREFS_Base, self).__init__()

		self.prefs = prefs
		self.filename = filename
		self.extension = extension

		self.separator = separator
		self.ender = ender
		self.continuer = continuer
		
		self.interpret = interpret
		self.dictionary = dictionary
		self.verbose = verbose
		self.cascade = cascade

		self.indent = indent
		self.comment = comment
		
		self.file = {}
		
		self.first_line = "#PREFS\n" # First line of all prefs file to recognize it.

	def check_file(self):
		"""
			Try to call read_prefs() method and if raises FileNotFoundError calls create_prefs() method.

			Returns:
				None
		"""

		try: # Try to open the file and if it doesn't exist create it

			self.read_prefs()

		except FileNotFoundError: # Except file not found create it

			if self.verbose: print(f"File not found. Trying to create {self.filename}")

			self.create_prefs(self.prefs) # Create PREFS file with default prefs dict

	def read_prefs(self) -> dict:
		"""Reads prefs file and returns it's value in a dictionary.

			Returns:
				A dictionary with all the prefs.
		"""

		if self.verbose: print(f"Trying to read {self.filename}")

		prefsTXT = open(f"{self.filename}.{self.extension}", "r") # Open the file with read permissions
		
		content = {} # Content will be where the prefs will be stored when reading
		lines = prefsTXT.readlines() # Read lines

		if not self.dictionary:
			content = self.get_lines_properties(lines) # Get lines properties (key, val, indentLevel)
			content = self.tree_to_dict(content) # Interpreting the result of get_lines_properties() returns the dictionary with the prefs. 
		
		elif self.dictionary:
			content = eval(lines[1])

		if self.interpret and not self.dictionary:
			content = self.eval_dict(content) # Pass content to eval_dict function that eval each value.

		prefsTXT.close() # Closing file

		if self.verbose: print(f"Read {self.filename}")

		self.file = content # Set self.file as content

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

			line = remove_comments(line, comment=self.comment)
			if not line.strip(): continue # If line emtpy continue

			indentLevel = len(line) - len(line.lstrip(self.indent)) # Count the indents of the line 
			keyVal = line.strip().split(self.separator) # Split the line by the default separator
			
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
				raise TypeError(f"self.prefs must be a dictionary or a function with a dictionary as return value, gived {type(prefs)}")
	
		if "/" in self.filename: # if "/" in filename means that if it's a path

			prefsPath = self.filename.split("/") # Split the path by / to iterate through

			for e, i in enumerate(prefsPath): # Iterate through the directory
				
				if e == len(prefsPath) - 1: break # If we are in the last element when split("/"), which means the filename break because isn't a folder
				
				if not path.isdir(i): os.mkdir(i) # If isn't the filename (last element) create folder if it doesn't exist

		prefsTXT = open(f"{self.filename}.{self.extension}","w+") # Opening the file with all permissions

		if self.verbose: print(f"Creating {self.filename}")

		prefsTXT.write(self.first_line) # First line will be self.first_line to recognize PREFS files
		
		lines = self.dict_to_tree(prefs) # Calls dict_to_tree() method which convert a dictionary into prefs file
		prefsTXT.write( lines ) # Writes the result of dict_to_tree() in the prefs file.

		prefsTXT.close() # Closing the file

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
		indent = self.indent * depth # Multiply depth by a tabulation, e.i.: if depth 0 no tabulation.

		if not self.dictionary: # If not dictionary format
			for key, val in prefs.items(): # Iterate through prefs dictionary items
				
				if isinstance(val, str) and self.interpret: # If value is a string and self.interpret write value with quotes
					result += f"{indent}{key}{self.separator}'{val}'{self.ender}" # Write key:value (str) with quotes

				elif isinstance(val, dict) and val != {} and self.cascade: # If values is a dictionary and cascade is True and isn't an empty dictionary

					result += f"{indent}{key}{self.separator}{self.continuer}\n" # Writes indent val and => to indicate that value in the text line.
					result += self.dict_to_tree(val, depth=depth + 1) # Calls itself to generate cascade/tree

				else: # If not self.interpret (and key isn't a string) write without quotes
					result += f"{indent}{key}{self.separator}{val}{self.ender}" # Write key:value in file

		if self.dictionary:
			return str(prefs)

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

		if string[0] == '"' and string[-1] == '"' or string[0] == "'" and string[-1] == "'": # If quotes string
			result = eval(string) # Evaluate string to get str type

		elif string == "True": # If string equals True return True
			result = True
		elif string == "False": # If string equals False return False
			result = False
		else: # If none of above types evaluate with eval
			result = eval(string)

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
		if not os.path.exists(f"{self.filename}.{self.extension}"):
			raise FileNotFoundError("Cannot overwrite unexistent prefs") # If file isn't in the path raise error

		if prefs is not None: # If prefs isn't none it must be a dictionary
			if not isinstance(prefs, dict):  # If isn't a dict raise error
				raise TypeError(f"prefs must be a dictionary or a function with a dictionary as return value, gived {type(prefs)}")

		if self.verbose: print(f"Trying to overwrite {self.prefs} in {self.filename}")

		self.delete_file() # Delete file to create it again

		if prefs == None: # If prefs equals None
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
		if not os.path.exists(f"{self.filename}.{self.extension}"): # If file isn't in the path raise error
			raise FileNotFoundError("Cannot change the name of a file that doesn't exists")
		
		if self.verbose: print(f"Trying to change {self.filename} name to {filename}")
		
		os.rename(f"{self.filename}.{self.extension}", f"{filename}.{self.extension}") # Rename file with os
		
		self.filename = filename # Change self.filename to passed filename

		if self.verbose: print(f"Changed filename to {self.filename}")

		self.check_file() # Read prefs to check the PREFS file and update file attribute 

	def delete_file(self) -> None:
		"""Deletes the prefs file (if you run your code again it will be created again).

		Returns:
			None

		"""
		if os.path.exists(f"{self.filename}.{self.extension}"): # If file is in the path

			if self.verbose: print(f"Trying to remove {self.filename}")
			
			os.remove(f"{self.filename}.{self.extension}") # Remove file
			
			if self.verbose: print(f"Removed {self.filename}")
			
			return # Return to break the function

		raise FileNotFoundError("Can't delete unexistent file") # Raise error because file isn't in the specified path

	def convert_to_json(self, filename: str="", extension: str="json", **kwargs) -> None:
		"""Converts the prefs file to a json file.
		
		Args:
			filename (str, optional=""): As default the same name as your prefs file but with .json extension.
			extension (str, option="json"): json file extension.

		Returns:
			None
		"""
		filename = self.filename if filename == "" else filename # If don't passed any filename set filename as self.filename, if filename passed set filename as filename 

		if self.verbose: print(f"Trying to dump {filename}.{extension}")

		with open(f"{filename}.{extension}", "w") as outfile: # Creating new json file
			json.dump(self.file, outfile, **kwargs) # Saving PREFS in json file
				
		if not os.path.isfile(f"{filename}.{extension}"): # If after create json file can't find it 
			warnings.RuntimeWarning(f"Can't find {filename}.{extension} after created") # Warn user

		if self.verbose: print(f"Successfuly created {filename}.{extension}")

	def convert_to_yaml(self, filename: str="", extension: str="yaml", **kwargs) -> None:
		"""Converts the prefs file into a yaml file.
		
		Args:
			filename (str, optional=""): As default the same name as your prefs file but with .yaml extension.
			extension (str, option="yaml"): yaml file extension.

		Returns:
			None
		"""

		filename = self.filename if filename == "" else filename # If don't passed any filename set filename as self.filename, if filename passed set filename as filename 

		if self.verbose: print(f"Trying to dump {filename}.{extension}")

		with open(f"{filename}.{extension}", "w") as outfile: # Creating new yaml file
			yaml.dump(self.file, outfile, **kwargs) # Saving PREFS in yaml file disablig sort_keys and default_flow_style
				
		if not os.path.isfile(f"{filename}.{extension}"): # If after create yaml file can't find it 
			warnings.RuntimeWarning(f"Can't find {filename}.{extension} after created") # Warn user

		if self.verbose: print(f"Successfuly created {filename}.{extension}")	

class PREFS(PREFS_Base): 
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

		convert_to_json(self, filename: str="", extension: str="json") -> None: Creates a json file with the actual prefs, if filename don't passed the prefs filename will be the json filename, returns None.
	
		convert_to_yaml(self, filename: str="", extension: str="yaml") -> None: Creates a yaml file with the actual prefs, if filename don't passed the prefs filename will be the yaml filename, returns None.
	"""
		
	def __init__(self, prefs: dict, filename: str="prefs", extension: str="prefs", separator: str="=", ender: str="\n", continuer: str=">", 
		interpret: bool=True, dictionary: bool=False, verbose: bool=False, cascade: bool=True, indent: str="\t"):
		
		"""	
		Args
			prefs (dict): A dictionary with the default preferences.
			filename (str, optional="prefs"): The name of the file (supports path).
			extension (str, optinal="prefs"): The extension of the file.
			separator (str, optional="="): The character between pref and value in the file.
			ender (str, optional="\n"): The character at the end of each pref:value.
			continuer (str, optional=">"): The character that precede a tree/cascade (nested dictionary).
			interpret (bool, optional=True): Interpret the value stored as python.
			dictionary (bool, optional=False): Writes the prefs as a python dictionary, no more human-readable (avoid any error at reading).
			verbose (bool, optional=False): Print logs all operations.
			cascade (bool, optional=True): Stores nested dictionaries as tree/cascade.
		"""
		
		super().__init__(prefs, filename=filename, extension=extension, 
			separator=separator, ender=ender, 
			continuer=continuer, interpret=interpret, 
			dictionary=dictionary, verbose=verbose, 
			cascade=cascade, indent=indent, 
			comment="#")

		"""self.prefs = prefs
		self.filename = filename
		self.extension = extension

		self.separator = separator
		self.ender = ender
		self.continuer = continuer
		
		self.interpret = interpret
		self.dictionary = dictionary
		self.verbose = verbose
		self.cascade = cascade
		
		self.file = {}
		
		self.first_line = "#PREFS\n" # First line of all prefs file to recognize it.
		"""
		
		#PREFS_Base.__init__(self, prefs, filename, extension, separator, ender, continuer, interpret, dictionary, verbose, cascade)

		self.check_file()
		
	def check_file(self):
		"""
			Try to call read_prefs() method and if raises FileNotFoundError calls create_prefs() method.

			Returns:
				None
		"""
		try: # Try to open the file and if it doesn't exist create it

			self.read_prefs()

		except FileNotFoundError: # Except file not found create it

			if self.verbose: print(f"File not found. Trying to create {self.filename}")

			self.create_prefs(self.prefs) # Create PREFS file with default prefs dict

def remove_comments(string: str, comment: str="#") -> str:
	"""Remove comments from strings (ignoring comments inside strings).

	Note:
		Iterates through the given string, if founds a quote and there isn't a backslash \ before it set in_string to True, if finds a # and in_string is False break the loop and cut the string until there and return it.
	Args:
		string (str): An string to remove the comments from
		comment: (str, optional="#"): Which character represents a comment

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

		if char == comment and not in_string: # If the current character is the comment character and isn't in a string
			string = string[:e] # Cut string until here
			break # And break

	return string # Return the string

def read_json_file(filename: str, extension: str="json", **kwargs) -> any:
	"""Reads Json files and returns it's value.

	Note:
		Object (dict) expected.

	Args:
		filename (str): The name of the json file to read
		extension (str, optional="json"): The extension of the json file.

	Returns:
		dict
	"""

	file = open(f"{filename}.{extension}", "r") # Open json file
	data = json.load(file, **kwargs) # Load json file
	file.close() # Close json file

	return data # Return data in the json file

def read_yaml_file(filename: str, extension: str="yaml", Loader=yaml.loader.SafeLoader, **kwargs) -> dict:
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
	
	with open(f"{filename}.{extension}") as file:
		data = yaml.load(file, Loader=Loader, **kwargs)

	return data 

def read_prefs_file(filename: str, extension: str="prefs", separator: str="=", ender: str="\n", continuer: str=">", 
		interpret: bool=True, dictionary: bool=False, verbose: bool=False, cascade: bool=True) -> dict:
	
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

	prefs_instance = PREFS_Base(prefs={}, filename=filename, extension=extension, 
			separator=separator, ender=ender, 
			continuer=continuer, interpret=interpret, 
			dictionary=dictionary, verbose=verbose, 
			cascade=cascade)

	return prefs_instance.read_prefs()

def convert_to_prefs(prefs: dict, separator: str="=", ender: str="\n", continuer: str=">", 
	interpret: bool=True, dictionary: bool=False, verbose: bool=False, cascade: bool=True, first_line: bool=False) -> str:
	
	"""Given a dictionary convert that dictionary into PREFS format and return it as string. 
	
	Args
		prefs (dict): A dictionary with the default preferences.
		separator (str, optional="="): The character between pref and value in the file.
		ender (str, optional="\n"): The character at the end of each pref:value.
		continuer (str, optional=">"): The character that precede a tree/cascade (nested dictionary).
		interpret (bool, optional=True): Interpret the value stored as python.
		dictionary (bool, optional=False): Writes the prefs as a python dictionary, no more human-readable (avoid any error at reading).
		verbose (bool, optional=False): Print logs all operations.
		cascade (bool, optional=True): Stores nested dictionaries as tree/cascade.

	Returns:
		A string contating the dictionary in PREFS format.

	"""

	prefs_instance = PREFS_Base(prefs=prefs, filename="", extension="", 
			separator=separator, ender=ender, 
			continuer=continuer, interpret=interpret, 
			dictionary=dictionary, verbose=verbose, 
			cascade=cascade)

	result = prefs_instance.first_line if first_line else ""
	result += prefs_instance.dict_to_tree(prefs)

	return result
