"""
PREFS is for store user preferences, in a simple and friendly way.
It has simple functions that you will understand fastly, also creates a total human readable file

Doesn't require any other library.

Content:
	PREFS (class): Instance this class to create a prefs file.
	ReadJsonFile(function): Simple function that reads a json file and returns it's value.
	GetStats(function): Shows you the PREFS library stats using pypistats (https://pypi.org/project/pypistats/).
"""


#Libraries
import os # To manage paths, folders and files
import json # To support export/import json files
import warnings # To send warnings
import pypistats # To see PREFS library stats in pypi
from os import path # To check if file or folder exists in path

class PREFS: 
	"""PREFS class creates a file to store and manage user preferences.
	
	Attributes:
		file(dict): easier way to get the ReadPrefs() returns value (to get the prefs).

	Methods:
		CheckFile() -> None: Try to call ReadPrefs() and if raises FileNotFoundError call CreatePrefs(), returns None.

		ReadPrefs() -> dict: Call GetLinesProperties and pass that value to TreeToDict to get the prefs inside the file. Returns the prefs in a dictionary.

		GetLinesProperties(lines: list) -> dict: Given a lines of a prefs file returns a dictionary with each line key, value and indentLevel.
		
		TreeToDict(ttree: dict, level: int=0) -> dict: Given the result of GetLinesProperties() interprets the indentLevel and returns a dictionary with the prefs.

		CreatePrefs(prefs: dict) -> None: Creates a file with the given prefs and the 
		PREFS class filename, returns None.

		WritePrefs(pref: str, value: any) -> None: Reading the prefs file as a dictionary 
		changes the passed pref to the passed value, if the pref (key) doesn't exist it 
		creates it. If using nested dictionaries calls ChangeNestedDictionaryVal() to change the given pref to the given value, returns None.

		ChangeNestedDictionaryVal(myDict: dict, keys: str, val: any) -> dict: Given a dictionary, a keys separeted by / and a value, search through the dictionary the keys and set the value, returns the dictionary with the changed value.

		OverWritePrefs(prefs: dict=None) -> None: Over writes the current prefs file 
		with the default prefs or if given a dictionary over writes the prefs file with it, returns None.

		ChangeFilename(filename: str) -> None: Changes the name of the prefs file 
		with the given one, returns None.

		DeleteFile() -> None: Removes the file if it exists, returns None.

		ConvertToJson(self, filename: str="", extension: str="json") -> None: Creates a json file with the actual prefs, if filename don't passed the prefs filename will be the json filename, returns None.
	"""
		
	def __init__(self, prefs: dict, filename: str="prefs", extension: str="prefs", separator: str="=", ender: str="\n", continuer: str=">", 
		interpret: bool=True, dictionary: bool=False, verbose: bool=False, cascade: bool=True): # encodeDecode: tuple=(None, None) # Encode Decode code disabled
		
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
			verbose (bool, optional=False): Pirnt logs all operations.
			cascade (bool, optional=True): Stores nested dictionaries as tree/cascade.
		"""
		# encodeDecode (tuple, optional=(None, None)): Tuple with first element encode function and second element decode function.
		
		super(PREFS, self).__init__()
		self.prefs = prefs
		self.filename = filename
		self.separator = separator
		self.ender = ender
		self.continuer = continuer
		self.interpret = interpret
		self.dictionary = dictionary
		self.verbose = verbose
		self.extension = extension
		self.file = {}
		# self.encodeDecode = encodeDecode # Encode Decode code disabled
		self.cascade = cascade
		self.depth = 0 # Indent level when creating prefs
		self.firstLine = "#PREFS\n" # First line of all prefs file to recognize it.

		"""
		# Encode Decode code disabled
		if callable(encodeDecode[0]) and callable(encodeDecode[1]):
			self.encodeDecodeBool = True
		else:
			raise TypeError(f"Incorrect encode and decode function, expected two functions, gived ({type(encodeDecode[0])}, {type(encodeDecode[1])})")
			self.encodeDecodeBool = False
		"""

		self.CheckFile()
		
	def CheckFile(self):
		"""
			Try to call ReadPrefs() method and if raises FileNotFoundError calls CreatePrefs() method.

			Returns:
				None
		"""
		try: # Try to open the file and if it doesn't exist create it

			self.ReadPrefs()

		except FileNotFoundError: # Except file not found create it

			if self.verbose: print(f"File not found. Trying to create {self.filename}")
			
			if callable(self.prefs): # If self.prefs is a function call it
				prefs = self.prefs() # Setting prefs to self.prefs function returns alue

			else: # If isn't callable
				prefs = self.prefs # Set prefs to self.prefs

			self.CreatePrefs(prefs) # Create PREFS file with prefs dict

	def ReadPrefs(self) -> dict:
		"""Reads prefs file and returns it's value in a dictionary.

			Returns:
				A dictionary with all the prefs.
		"""

		if self.verbose: print(f"Trying to read {self.filename}")

		prefsTXT = open(f"{self.filename}.{self.extension}", "r") # Open the file with read permissions
		
		content = {} # Content will be where the prefs will be stored when reading
		lines = prefsTXT.readlines() # Read lines

		content = self.GetLinesProperties(lines) # Get lines properties (key, val, indentLevel)
		content = self.TreeToDict(content) # Interpreting the result of GetLinesProperties() returns the dictionary with the prefs. 
		
		"""
		# Encode Decode code disabled
		if self.encodeDecodeBool:
			content = self.DecodeDict(content)
		"""
		if self.interpret:
			content = self.EvalDict(content) # Pass content to EvalDict function that eval each value.

		prefsTXT.close() # Closing file

		if self.verbose: print(f"Read {self.filename}")

		self.file = content # Set self.file as content

		return content # Return prefs file as dictionary

	# The below code is from https://stackoverflow.com/questions/17858404/creating-a-tree-deeply-nested-dict-from-an-indented-text-file-in-python/24966533#24966533
	def GetLinesProperties(self, lines: list) -> dict:
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

	def TreeToDict(self, ttree: dict, level: int=0) -> dict:
		"""Given the result of GetLinesProperties() returns a dictionary with the prefs.

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
				self.DictInsertOrAppend(result, cn['key'], cn['val'])
			
			elif nn['indentLevel'] > level:
				rr = self.TreeToDict(ttree[i + 1:], level=nn['indentLevel'])
				self.DictInsertOrAppend(result, cn['key'], rr)

			else:    
				self.DictInsertOrAppend(result, cn['key'], cn['val'])
		
				return result
		
		return result

	def DictInsertOrAppend(self, adict: dict, key: str, val: any):
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

	def CreatePrefs(self, prefs: dict) -> None:
		"""Creates a file with the prefs that you pass.

			Args:
				prefs (dict): The prefs that will write in the file.

			Returns:
				None
		"""

		if not isinstance(prefs, dict): # If isn't a dict raise error
				raise TypeError(f"self.prefs must be a dictionary or a function with a dictionary as return value, gived {type(prefs)}")
	
		if "/" in self.filename: # if "/" in filename means that if it's a path

			prefsPath = self.filename.split("/") # Split the path by / to iterate through

			for e, i in enumerate(prefsPath): # Iterate through the directory
				
				if e == len(prefsPath) - 1: break # If we are in the last element when split("/"), which means the filename break because isn't a folder
				
				if not path.isdir(i): os.mkdir(i) # If isn't the filename (last element) create folder if it doesn't exist

		prefsTXT = open(f"{self.filename}.{self.extension}","w+") # Opening the file with all permissions

		if self.verbose: print(f"Creating {self.filename}")

		prefsTXT.write(self.firstLine) # First line will be self.firstLine to recognize PREFS files

		
		lines = self.DictToText(prefs) # Calls DictToText() method which convert a dictionary into prefs file
		prefsTXT.write( lines ) # Writes the result of DictToText() in the prefs file.

		prefsTXT.close() # Closing the file

		if self.verbose: print(f"{self.filename} created")

		self.CheckFile() # Read prefs to check the PREFS file and update file attribute 

	def DictToText(self, prefs: dict, indent: str="") -> str:
		"""Converts the prefs dictionary to prefs file.

			Args:
				prefs (dict): a dictionary with the prefs to convert to text.
				indent (str=""): How much indent the text

			Returns:
				An string with the prefs, ready to write.
		"""	
		result = "" # String to append each pref:value combination

		if not isinstance(prefs, dict): # If isn't a dict raise error
				raise TypeError(f"prefs argument must be a dictionary or a function with a dictionary as return value, gived {type(prefs)}")
		
		"""
		# Encode Decode code disabled
		if self.encodeDecodeBool:
			prefs = self.EncodeDict(prefs)
		"""

		if not self.dictionary: # If not dictionary format
			for key, val in prefs.items(): # Iterate through prefs dictionary items
				
				if isinstance(val, str) and self.interpret: # If value is a string and self.interpret write value with quotes
					result += f"{indent}{key}{self.separator}'{val}'{self.ender}" # Write key:value (str) with quotes

				elif isinstance(val, dict) and self.cascade: # If values is a dictionary and cascade is True
					keyIndent = "\t" * self.depth # Indent string depending on depth of line

					result += f"{keyIndent}{key}{self.separator}{self.continuer}\n" # Writes indent val and => to indicate that value in the text line.
					self.depth += 1 # Adds one to depth
					result += self.DictToText(val, indent="\t" * self.depth) # Calls itself to generate cascade/tree

				else: # If not self.interpret (and key isn't a string) write without quotes
					result += f"{indent}{key}{self.separator}{val}{self.ender}" # Write key:value in file

		self.depth -= 1 if self.depth > 0 else 0 # Subtracts one to depth if is greater than 0
		return result

		self.CheckFile() # Read prefs to check the PREFS file and update file attribute 

	def EvalDict(self, prefs: dict) -> dict:
		"""Evaluate dict with strings representing python types (using EvalString() method).

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
				result[key] = self.EvalDict(val) # Using recursive function to get all values in cascade/tree.
				continue

			result[key] = self.EvalString(val) # If don't dictionary call EvalString() method.

		return result

	def EvalString(self, string: str) -> any:
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

	"""
	# Encode Decode code disabled
	def EncodeDict(self, myDict: dict) -> dict:
		if not self.encodeDecodeBool:
			return myDict

		result = {}

		for key, val in myDict.items():
			if isinstance(val, dict):
				result[key] = self.EncodeDict(val)
				continue
			result[key] = self.encodeDecode[0](val)

		return result

	def DecodeDict(self, myDict: dict) -> dict:
		if not self.encodeDecodeBool:
			return myDict

		result = {}

		for key, val in myDict.items():
			if isinstance(val, dict):
				result[key] = self.DecodeDict(val)
				continue
			result[key] = self.encodeDecode[1](val)

		return result
		"""

	def WritePrefs(self, pref: str, value: any) -> None:
		"""Change the pref that you pass with the value that you pass, if doesn't exist, new pref.
			To change nested dictionary pass path, e.g.: WritePrefs(pref="keybindings/Copy", value="ctrl+c")
			
			Args:
				pref (str): the name of the pref that you want to change, if it doesn't exist, it will create it.
				value (any): the value that you want to assign to the pref.

			Returns:
				None

		"""

		if self.verbose: print(f"Trying to write {pref} with {value} value in {self.filename}")
		
		content = self.ReadPrefs() # Get prefs dictionary

		if "/" in pref: # If / in pref means that prefs is a nested dictionary
			content = self.ChangeNestedDictionaryVal(content, pref, value) # Calls method that change value of nested dictionaries.
		else: # If not / in pref
			content[pref] = value # Simply change pref to given value


		self.CreatePrefs(content) # Replace old file with updated file

		if self.verbose: print(f"Writed {pref} with {value} value in {self.filename}")

		self.CheckFile() # Read prefs to check the PREFS file and update file attribute 

	def ChangeNestedDictionaryVal(self, myDict: dict, keys: str, val: any) -> dict:
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

	def OverWritePrefs(self, prefs: dict = None) -> None:
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

		self.DeleteFile() # Delete file to create it again

		if prefs == None: # If prefs equals None
			self.CreatePrefs(self.prefs) # Create prefs with default value
		elif isinstance(prefs, dict): # If isn't none is because you have passed an argument so create the new file with the passed prefs
			self.CreatePrefs(prefs) # Create prefs file with given dictionary

		if self.verbose: print(f"Overwrited {self.prefs} in {self.filename}")

		self.CheckFile() # Read prefs to check the PREFS file and update file attribute 
			
	def ChangeFilename(self, filename: str) -> None:
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

		self.CheckFile() # Read prefs to check the PREFS file and update file attribute 

	def DeleteFile(self) -> None:
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

	def ConvertToJson(self, filename: str="", extension: str="json") -> None:
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
			json.dump(self.file, outfile) # Saving PREFS in json file
				
		if not os.path.isfile(f"{filename}.{extension}"): # If after create json file can't find it 
			warnings.RuntimeWarning(f"Can't find {filename}.{extension} after created") # Warn user

		if self.verbose: print(f"Successfuly created {filename}.{extension}")

def ReadJsonFile(filename: str, extension: str="json"):
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
	data = json.load(file) # Load json file
	file.close() # Close json file

	return data # Return data in the json file

def GetStats(mode: str="overall", period: str="", mirrors: bool=None, version: str="", os: str="", format: str="markdown"):
	"""Shows you the stats of the PREFS library using pypistats (https://pypi.org/project/pypistats/).
	
	Args:
		mode (str, optional="overall"): [recent, overall, python_major, python_minor, system]
		period (str, optional): [day, week, month]
		format (str, optional): [json, markdown, rst, html]
		mirrors (bool, optional): Show overall stats with mirrors.
		version (str): Python version to show stats. 

	Returns:
		str: pypistats string with prefs stats
	"""
	if mode == "overall": # If overall mode
		data = pypistats.overall("prefs", mirrors=mirrors, format=format) # Get stats of PREFS library with pypi stats
		print(data) # Print stats
		return data # Return stats
	elif mode == "recent": # If recent mode
		data = pypistats.recent("prefs", period, format=format) # Get stats of PREFS library with pypi stats
		print(data) # Print stats 
		return data # Return stats
	elif mode == "python_major": # If python_major mode
		data = pypistats.python_major("prefs", version=version, format=format) # Get stats of PREFS library with pypi stats
		print(data) # Print stats
		return data # Return stats
	elif mode == "python_minor": # If python_minor mode
		data = pypistats.python_minor("prefs", version=version, format=format) # Get stats of PREFS library with pypi stats
		print(data) # Print stats
		return data # Return stats
	elif mode == "system": # If system mode
		data = pypistats.system("prefs", os=os, format=format) # Get stats of PREFS library with pypi stats
		print(data) # Print stats
		return data # Return stats
	else: # If mode isn't any supported by pypistats raise error
		raise ValueError(f"pypistats doesn't support {mode}") # Raise error
