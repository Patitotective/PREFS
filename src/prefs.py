# src/prefs.py

# Libraries
import os
import ast
import json
import yaml
from collections import UserDict

# Dependencies
from src.utils import check_path

class PrefsBase(UserDict):
	FIRST_LINE = "#PREFS"
	SEPARATOR_CHAR = "="
	ENDER_CHAR = "\n"
	CONTINUER_CHAR = ">"
	COMMENT_CHAR = "#"
	INDENT_CHAR = "\t"
	AUTO_GEN_KEYS = True

	def __init__(self, prefs: dict[str, any], path: str):
		super().__init__(prefs)

		self.prefs = prefs
		self.path = path

	def __dict__(self):
		return self.read_prefs()

	def __getitem__(self, key):
		return self.__dict__[key]

	def __setitem__(self, key, value):
		self.write_prefs(key, value)

	def check_file(self):
		"""Try to call read_prefs() method and if raises FileNotFoundError calls create_prefs() method.

		Returns:
			None
		"""

		if os.path.isfile(self.path): # Try to open the file and if it doesn't exist create it
			return self.read_prefs()

		self.create_prefs(self.prefs) # Create Prefs file with default prefs dict

	def read_prefs(self, filename=None) -> dict:
		"""Reads prefs file and returns it's value in a dictionary.
	
		Parameters:
			filename=None: the filename of the prefs file to read, if no specified self.path.

		Returns:
			A dictionary with all the prefs.
		"""
		if filename is None:
			filename = self.path

		content = {} # Content will be where the prefs will be stored when reading

		with open(filename, "r") as file: # Open the file with read permissions
			lines = file.read().split("\n") # Read lines

			if len(lines) == 0:
				return {}

			content = self.tree_to_dict(lines) # Interpreting the result of get_lines_properties() returns the dictionary with the prefs. 

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
					raise SyntaxError(f"Could not read line {get_line_num(line_num)}: \n\t{line.strip()}\nin {self.path} file (hint: empty key or value)")

			except ValueError:
				raise SyntaxError(f"Could not read line {get_line_num(line_num)}: \n\t{raw_line.strip()}\nin {self.path} file (hint: missing separator {self.SEPARATOR_CHAR!r})")

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
				if len(string) == 0:
					return string # If empty string return empty

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
				warnings.warn(f"Repeated key {line_info['key']!r} at {get_line_num(line_num)}", SyntaxWarning)

			## Eval value ##
			if line_info["val"] != self.CONTINUER_CHAR:
				try:
					line_info["val"] = eval_val(line_info["val"])
				except (SyntaxError, ValueError):
					raise SyntaxError(f"Could not eval line {get_line_num(line_num)}: \n\t{raw_line.strip()}\nin {self.path}")

			## Check for indentation errors and next line ##
			if line_num < len(lines) - 1 and not clean_line(lines[line_num + 1]) is None:
				raw_next_line = lines[line_num + 1]
				next_line = clean_line(raw_next_line)
							
				next_line_info = get_line_info(next_line, raw_next_line, line_num + 1)
				if line_info['val'] == self.CONTINUER_CHAR and next_line_info["indent_level"] != line_info["indent_level"] + 1:
					raise IndentationError(f"Expected indent block after line ~{get_line_num(line_num)} (remember to indent with tabulations)")
				
				if next_line_info["indent_level"] == line_info["indent_level"] + 1 and line_info["val"] != self.CONTINUER_CHAR:
					raise IndentationError(f"Unexpected indentation found at line {get_line_num(line_num + 1)}: \n\t{lines[line_num + 1].strip()}\nin {self.path}")

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

		result = f"{self.FIRST_LINE}{self.ENDER_CHAR}"
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
	
		check_path(self.path)

		with open(self.path, "w+") as prefs_file: # Opening the file with all permissions
			prefs_file.write(f"{self.FIRST_LINE}{self.ENDER_CHAR}") # First line will be self.FIRST_LINE to recognize Prefs files
			
			lines = self.dict_to_tree(prefs) # Calls dict_to_tree() method which convert a dictionary into prefs file
			prefs_file.write(lines) # Writes the result of dict_to_tree() in the prefs file.

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

	def write_prefs(self, key: str, val: any) -> None:
		"""Change the key that you pass with the value that you pass, if doesn't exist, new key.
			To change nested dictionary pass path, e.g.: write_prefs(key="keybindings/Copy", val="ctrl+c")
			
			Args:
				key (str): the name of the key that you want to change, if it doesn't exist, it will create it.
				val (any): the value that you want to assign to the key.

			Returns:
				None

		"""
		prefs = self.__dict__()
		prefs[key] = val # Simply change key to given value

		self.create_prefs(prefs) # Replace old file with updated file

		self.check_file() # Read prefs to check the Prefs file and update file attribute 

	def write_multiple_prefs(self, prefs: dict[str, any]) -> None:
		"""Given a list of prefs and a list of values, cahnges all prefs with it's corresponding value (like write_prefs).
		This way is more eficiently that opening and closing a file 10 times.
			
		Args:
			prefs: Dict[str, any]

		Returns:
			None
		"""		
		content = self.read_prefs() # Get prefs dictionary

		for pref, value in prefs.items():
			if "/" in pref: # If / in pref means that prefs is a nested dictionary
				content = self.change_nested_dict_val(content, pref, value) # Calls method that change value of nested dictionaries.
			else: # If not / in pref
				content[pref] = value # Simply change pref to given value

		self.create_prefs(content) # Replace old file with updated file

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
		if not os.path.isfile(self.path):
			raise FileNotFoundError("Cannot overwrite unexistent prefs") # If file isn't in the path raise error

		if prefs is not None: # If prefs isn't none it must be a dictionary
			if not isinstance(prefs, dict):  # If isn't a dict raise error
				raise TypeError(f"prefs must be a dictionary or a function with a dictionary as return value, gived {type(prefs)}")

		self.delete_file() # Delete file to create it again

		if prefs is None:
			self.create_prefs(self.prefs) # Create prefs with default value
		elif isinstance(prefs, dict): # If isn't none is because you have passed an argument so create the new file with the passed prefs
			self.create_prefs(prefs) # Create prefs file with given dictionary

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
		if not os.path.isfile(self.path): # If file isn't in the path raise error
			raise FileNotFoundError("Cannot change the name of a file that doesn't exists")
				
		os.rename(self.path, filename) # Rename file with os
		
		self.path = filename # Change self.path to passed filename

		self.check_file() # Read prefs to check the Prefs file and update file attribute 

	def delete_file(self) -> None:
		"""Deletes the prefs file (if you run your code again it will be created again).

		Returns:
			None

		"""
		if not os.path.isfile(self.path): # If file is in the path
			raise FileNotFoundError("Can't delete unexistent file") # Raise error because file isn't in the specified path
		
		os.remove(self.path) # Remove file
		
	def convert_to_json(self, filename: str=None, **kwargs) -> None:
		"""Converts the prefs file to a json file.
		
		Args:
			filename (str, optional=""): As default the same name as your prefs file but with .json extension.

		Returns:
			None
		"""
		# If don't passed any filename set filename as self.path, if filename passed set filename as filename 
		if filename is None:
			filename = f"{os.path.splitext(self.path)[0]}.json"

		with open(filename, "w") as outfile: # Creating new json file
			json.dump(self.file, outfile, **kwargs) # Saving Prefs in json file

	def convert_to_yaml(self, filename: str=None, **kwargs) -> None:
		"""Converts the prefs file into a yaml file.
		
		Args:
			filename (str, optional=""): As default the same name as your prefs file but with .yaml extension.
		Returns:
			None
		"""

		# If don't passed any filename set filename as self.path, if filename passed set filename as filename 
		if filename is None:
			filename = f"{os.path.splitext(self.path)[0]}.yaml"

		with open(filename, "w") as outfile: # Creating new yaml file
			yaml.dump(self.file, outfile, **kwargs) # Saving Prefs in yaml file disablig sort_keys and default_flow_style


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
		

if __name__ == "__main__":
	prefs = PrefsBase({}, "trial/prefs.prefs")
	prefs["a"] = 1
	print(prefs)
