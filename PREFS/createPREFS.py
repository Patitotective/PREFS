"""This script is a little instance that simulate to create a PREFS file but instead of writting the PREFS returns the text (that should be written in the PREFS file) 
"""

#Libraries
import os # To manage paths, folders and files
from os import path # To check if file or folder exists in path

class CreatePREFS: 
	"""PREFS class creates a file to store and manage user preferences.
	
	Attributes:
		file(dict): easier way to get the ReadPrefs() returns value (to get the prefs).

	Methods:
		CheckFile() -> None: Try to call ReadPrefs() and if raises FileNotFoundError call create_prefs(), returns None.

		ReadPrefs() -> dict: Call GetLinesProperties and pass that value to TreeToDict to get the prefs inside the file. Returns the prefs in a dictionary.

		GetLinesProperties(lines: list) -> dict: Given a lines of a prefs file returns a dictionary with each line key, value and indentLevel.
		
		TreeToDict(ttree: dict, level: int=0) -> dict: Given the result of GetLinesProperties() interprets the indentLevel and returns a dictionary with the prefs.

		create_prefs(prefs: dict) -> None: Creates a file with the given prefs and the 
		PREFS class filename, returns None.
	"""
		
	def __init__(self, prefs: dict, separator: str="=", ender: str="\n", continuer: str=">", 
		interpret: bool=True, dictionary: bool=False, verbose: bool=False, cascade: bool=True): 
		
		"""	
		Args
			prefs (dict): A dictionary with the default preferences.
			separator (str, optional="="): The character between pref and value in the file.
			ender (str, optional="\n"): The character at the end of each pref:value.
			continuer (str, optional=">"): The character that precede a tree/cascade (nested dictionary).
			dictionary (bool, optional=False): Writes the prefs as a python dictionary, no more human-readable (avoid any error at reading).
			verbose (bool, optional=False): Print logs all operations.
			cascade (bool, optional=True): Stores nested dictionaries as tree/cascade.
		"""

		super(CreatePREFS, self).__init__()
		self.prefs = prefs

		self.separator = separator
		self.ender = ender
		self.continuer = continuer
		
		self.interpret = interpret
		self.dictionary = dictionary
		self.verbose = verbose
		self.cascade = cascade
		
		self.file = {}
		self.depth = 0 # Indent level when creating prefs
		
		self.firstLine = "#PREFS\n" # First line of all prefs file to recognize it.

	def create_prefs(self, prefs: dict=None) -> None:
		"""Creates a file with the prefs that you pass.

			Args:
				prefs (dict): The prefs that will write in the file.

			Returns:
				None
		"""
		if prefs == None:
			prefs = self.prefs

		if callable(prefs): # If self.prefs is a function call it
			prefs = prefs() # Setting prefs to self.prefs function returns alue

		if not isinstance(prefs, dict): # If isn't a dict raise error
				raise TypeError(f"self.prefs must be a dictionary or a function with a dictionary as return value, gived {type(prefs)}")


		if self.verbose: print(f"Converting to PREFS")
		result = ""

		result += self.firstLine # First line will be self.firstLine to recognize PREFS files

		
		lines = self.dict_to_text(prefs) # Calls dict_to_text() method which convert a dictionary into prefs file
		result += lines # Writes the result of dict_to_text() in the prefs file.

		if self.verbose: print(f"PREFS created")

		return result

	def dict_to_text(self, prefs: dict, indent: str="") -> str:
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
		
		if not self.dictionary: # If not dictionary format
			for key, val in prefs.items(): # Iterate through prefs dictionary items
				
				if isinstance(val, str) and self.interpret: # If value is a string and self.interpret write value with quotes
					result += f"{indent}{key}{self.separator}'{val}'{self.ender}" # Write key:value (str) with quotes

				elif isinstance(val, dict) and self.cascade: # If values is a dictionary and cascade is True
					keyIndent = "\t" * self.depth # Indent string depending on depth of line

					result += f"{keyIndent}{key}{self.separator}{self.continuer}\n" # Writes indent val and => to indicate that value in the text line.
					self.depth += 1 # Adds one to depth
					result += self.dict_to_text(val, indent="\t" * self.depth) # Calls itself to generate cascade/tree

				else: # If not self.interpret (and key isn't a string) write without quotes
					result += f"{indent}{key}{self.separator}{val}{self.ender}" # Write key:value in file

		if self.dictionary:
			return str(prefs)

		self.depth -= 1 if self.depth > 0 else 0 # Subtracts one to depth if is greater than 0
		return result
