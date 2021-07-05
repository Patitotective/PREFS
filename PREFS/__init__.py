#!/usr/bin/env python3

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
import ast
import os
import json
import warnings
import pypistats
from os import path

class PREFS(object): 
	"""PREFS class creates a file to store and manage user preferences.
	
	Attributes:
		file(dict): easier way to get the ReadPrefs() returns value (to get the prefs).

	Methods:
		ReadPrefs() -> dict: Returns a dictionary reading the file where the prefs are 
		stored, if this file doesn't exist it will create it.

		ReadOneLine(lines: list) -> dict: Given a list of lines returns the first line 
		as a dictionary.

		CreatePrefs(prefs: dict) -> None: Create a file with the given prefs and the 
		class filename, returns None.

		WritePrefs(pref: str, value: any) -> None: Reading the prefs file as a dictionary 
		changes the passed pref to the passed value, if the pref (key) doesn't exist it 
		creates it, returns None.

		OverWritePrefs(prefs: dict=None) -> None: Over write the current prefs file 
		with the given dictionary or without passing anything reset the prefs to the 
		defaults, returns None.

		ChangeFilename(filename: str) -> None: Changes the name of the prefs file 
		with the given one, returns None.

		DeleteFile() -> None: Removes the file if it exists, returns None.
	"""
		
	def __init__(self, prefs: dict, filename: str="prefs", extension: str="txt", separator: str="=", ender: str="\n", 
		interpret: bool=False, dictionary: bool=False, debug: bool=False):
		
		"""	
		Args
			prefs (dict): A dictionary with the default preferences.
			filename (str, optional="prefs"): The name of the file (can include path).
			extension (str, optinal="txt"): The extension of the file.
			separator (str, optional="="): The character between pref and value in the file.
			ender (str, optional="\n"): The character at the end of each pref:value.
			interpret (bool, optional=False): Interpret the value stored as python.
			dictionary (bool, optional=False): Writes the prefs as a python dictionary (avoid any error at reading).
			debug (bool, optional=False): Print messages of all operations.
		"""
		
		super(PREFS, self).__init__()
		self.prefs = prefs
		self.filename = filename
		self.separator = separator
		self.ender = ender
		self.interpret = interpret
		self.dictionary = dictionary
		self.debug = debug
		self.extension = extension
		self.file = None

		self.ReadPrefs()
		
	def ReadPrefs(self) -> str:
		"""
			Try to read the prefs and if the file doesn't exist call the CreatePrefs() function to create it.

			Returns:
				A dictionary with all the prefs.
		"""
		try:
			if self.debug: print(f"Trying to read {self.filename}")

			prefsTXT = open(f"{self.filename}.{self.extension}", "r")
			
			content = {}
			lines = prefsTXT.readlines()
			lines1 = []

			if lines[0] != "#PREFS\n": raise TypeError("Cannot read the file, check the file ('#PREFS' must be the first line)")

			if not self.dictionary:
				e = 0
				for line in lines:
					if line[0] == "#": continue
					lines1.append(line.replace(self.ender, ""))

					if not self.interpret:
						content[lines1[e].split(self.separator, 1)[0]] = lines1[e].split(self.separator, 1)[1]
					elif self.interpret:
						content[ lines1[e].split(self.separator, 1)[0] ] = ast.literal_eval( lines1[e].split(self.separator, 1)[1] )

					e += 1

			elif self.dictionary:
				content = ast.literal_eval(lines[1])

			prefsTXT.close()

			if self.debug: print(f"Read {self.filename}")

			self.file = content
			return content

		except FileNotFoundError:
			if self.debug: print(f"File not found. Trying to create {self.filename}")
			if (callable(self.prefs)): self.CreatePrefs(self.prefs())
			else: self.CreatePrefs(self.prefs)

	def CreatePrefs(self, prefs: dict) -> None:
		"""
			Creates a file with the prefs that you pass.

			Args:
				prefs (dict): The prefs that will write in the file.

			Returns:
				None
		"""
		if "/" in self.filename:
			for e, i in enumerate(self.filename.split("/")):
				if e == len(self.filename.split("/")) - 1: break 
				if not path.isdir(i): os.mkdir(i)

		prefsTXT = open(f"{self.filename}.{self.extension}","w+")

		if self.debug: print(f"Creating {self.filename}")

		prefsTXT.write("#PREFS\n")

		if not self.dictionary:
			for i in prefs.items():
				if isinstance(i[1], str) and self.interpret: prefsTXT.write(f"{i[0]}=\"{i[1]}\"{self.ender}")
				else: prefsTXT.write(f"{i[0]}={i[1]}{self.ender}")

		elif self.dictionary:
			prefsTXT.write(str(prefs))

		prefsTXT.close()

		if self.debug: print(f"{self.filename} created")

		self.ReadPrefs()

	def WritePrefs(self, pref: str, value: any) -> None:
		"""
			Change the pref that you pass with the value that you pass, if doesn't exist, new pref.
			
			Args:
				pref (str): the name of the pref that you want to change, if it doesn't exist, it will create it.
				value (any): the value that you want to assign to the pref.

			Returns:
				None

		"""

		if self.debug: print(f"Trying to write {pref} with {value} value in {self.filename}")
		content = self.ReadPrefs()
		content[pref] = value

		self.CreatePrefs(content)

		if self.debug: print(f"Writed {pref} with {value} value in {self.filename}")

		self.ReadPrefs()

	def OverWritePrefs(self, prefs: dict = None) -> None:
		"""
			Changes the prefs with the prefs that you pass or if you don't pass nothing reset the current prefs (with the values at initializing).
			
			Args:
				prefs (dict, optional): New prefs, if empty reset prefs.

			Returns:
				None  
		"""
		if os.path.exists(f"{self.filename}.{self.extension}"):

			if self.debug: print(f"Trying to write {self.prefs} in {self.filename}")

			os.remove(f"{self.filename}.{self.extension}")
			if prefs == None:
				self.CreatePrefs(self.prefs)
			else:
				self.CreatePrefs(prefs)

			if self.debug: print(f"Overwrited {self.prefs} in {self.filename}")

		else: raise FileNotFoundError("Cannot overwrite unexistent prefs")

		self.ReadPrefs()
			
	def ChangeFilename(self, filename: str) -> None:
		"""Changes the name of the file.
		
		Note:
			The filename will be changed but you have to change it's name at class init.

		Args:
			filename (str): the new name of the file.

		Returns:
			None

			"""
		if not os.path.exists(f"{self.filename}.{self.extension}"): raise FileNotFoundError("Cannot change the name of a file that doesn't exists")
		if self.debug: print(f"Trying to change {self.filename} name to {filename}")
		
		os.rename(f"{self.filename}.{self.extension}", f"{filename}.{self.extension}")
		self.filename = filename

		if self.debug: print(f"Changed filename to {self.filename}")

		self.ReadPrefs()

	def DeleteFile(self) -> None:
		"""Deletes the prefs file (if you run your code again it will be created again).

		Returns:
			None

		"""
		if os.path.exists(f"{self.filename}.{self.extension}"):
			if self.debug: print(f"Trying to remove {self.filename}")
			os.remove(f"{self.filename}.{self.extension}")
			if self.debug: print(f"Removed {self.filename}")
			return

		raise FileNotFoundError("Can't delete unexistent file")

	def ConvertToJson(self, filename: str="", extension: str="json") -> None:
		"""Converts the prefs file to a json file.
		
		Args:
			filename (str, optional=""): As default the same name as your prefs file but with .json extension.
			extension (str, option="json"): json file extension.

		Returns:
			None
		"""
		filename = self.filename if filename == "" else filename

		if self.debug: print(f"Trying to dump {filename}.{extension}")

		with open(f"{filename}.{extension}", "w") as outfile: 
		    json.dump(self.file, outfile)
				
		if not os.path.isfile(f"{filename}.{extension}"): warnings.RuntimeWarning(f"Can't find {filename}.{extension}")

		if self.debug: print(f"Successfuly created {filename}.{extension}")

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

	file = open(f"{filename}.{extension}", "r")
	data = json.load(file)
	file.close()

	return data

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
	if mode == "overall":
		data = pypistats.overall("prefs", mirrors=mirrors, format=format)
		print(data)
		return data
	elif mode == "recent":
		data = pypistats.recent("prefs", period, format=format)
		print(data)
		return data
	elif mode == "python_major":
		data = pypistats.python_major("prefs", version=version, format=format)
		print(data)
		return data
	elif mode == "python_minor":
		data = pypistats.python_minor("prefs", version=version, format=format)
		print(data)
		return data
	elif mode == "system":
		data = pypistats.system("prefs", os=os, format=format)
		print(data)
		return data		
