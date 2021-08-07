"""This script creates is a little isntance of PREFS class that only reads a file.
"""


#Libraries
import os # To manage paths, folders and files
from os import path # To check if file or folder exists in path

class ReadPREFS: 
	"""ReadPREFS class reads a PREFS file.
	
	Attributes:
		file(dict): easier way to get the read_prefs() returns value (to get the prefs).

	Methods:
		check_file() -> None: Try to call read_prefs() and if raises FileNotFoundError call CreatePrefs(), returns None.

		read_prefs() -> dict: Call get_lines_properties and pass that value to tree_to_dict to get the prefs inside the file. Returns the prefs in a dictionary.

		get_lines_properties(lines: list) -> dict: Given a lines of a prefs file returns a dictionary with each line key, value and indentLevel.
		
		tree_to_dict(ttree: dict, level: int=0) -> dict: Given the result of get_lines_properties() interprets the indentLevel and returns a dictionary with the prefs.
	"""
		
	def __init__(self, filename: str, extension: str="prefs", separator: str="=", ender: str="\n", continuer: str=">", 
		interpret: bool=True, dictionary: bool=False, verbose: bool=False, cascade: bool=True):
		
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

		super(ReadPREFS, self).__init__()
		self.filename = filename
		self.separator = separator
		self.ender = ender
		self.continuer = continuer
		self.interpret = interpret
		self.dictionary = dictionary
		self.verbose = verbose
		self.extension = extension
		self.file = {}
		self.cascade = cascade
		self.depth = 0 # Indent level when creating prefs
		self.firstLine = "#PREFS\n" # First line of all prefs file to recognize it.


		self.check_file()
		
	def check_file(self):
		"""
			Try to call read_prefs() method and if raises FileNotFoundError calls CreatePrefs() method.

			Returns:
				None
		"""
		try: # Try to open the file and if it doesn't exist create it

			self.read_prefs()

		except FileNotFoundError: # Except file not found create it

			raise FileNotFoundError(f"{self.filename} file not found")

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
		if lines[0] != self.firstLine: raise TypeError("Cannot read the file, it could be corrupted ('#PREFS' must be the first line)")

		for e, line in enumerate(lines): # Iterate through the lines (of the file)

			if line[0].strip() == "#": continue # If first character is # ignore the whole line		

			indentLevel = len(line) - len(line.lstrip('\t')) # Count the indents of the line 
			keyVal = line.strip().split(self.separator) # Split the line by the default separator
		
			result.append({"key": keyVal[0], "val": keyVal[1], "indentLevel": indentLevel}) # Append the above values in dict format to the result list

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
		
		for i in range(0, len(ttree)):
			cn = ttree[i]
			
			try:
				nn  = ttree[i+1]
			except:
				nn = {'indentLevel': -1}

			# Edge cases
			if cn['indentLevel'] > level:
				continue
			
			if cn['indentLevel'] < level:
				return result

			# Recursion
			if nn['indentLevel'] == level:
				self.dict_insert_or_append(result, cn['key'], cn['val'])
			
			elif nn['indentLevel'] > level:
				rr = self.tree_to_dict(ttree[i + 1:], level=nn['indentLevel'])
				self.dict_insert_or_append(result, cn['key'], rr)

			else:    
				self.dict_insert_or_append(result, cn['key'], cn['val'])
		
				return result
		
		return result

	def dict_insert_or_append(self, adict: dict, key: str, val: any):
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

		for key, val in prefs.items(): # Iterate through prefs dictionary
		
			if isinstance(val, dict): # If dictionary type calls itself to evaluate
				result[key] = self.eval_dict(val) # Using recursive function to get all values in cascade/tree.
				continue

			result[key] = self.eval_string(val) # If don't dictionary call eval_string() method.

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
