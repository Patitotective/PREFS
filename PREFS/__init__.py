#!/usr/bin/env python3

"""
PREFS is for store user preferences, in a simple and friendly way.
It has simple functions that you will understand fastly, also creates a total human readable file

Doesn't require any other library.

Content:
	PREFS (class): Instance this class to create a prefs file.

"""


#Libraries
import ast
import os
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

			if not self.dictionary:
				if len(lines) > 1:
					e = 0
					for line in lines:
						lines1.append(line.replace(self.ender, ""))

						if not self.interpret:
							content[lines1[e].split(self.separator, 1)[0]] = lines1[e].split(self.separator, 1)[1]
						elif self.interpret:
							content[ lines1[e].split(self.separator, 1)[0] ] = ast.literal_eval( lines1[e].split(self.separator, 1)[1] )

						e += 1

				elif len(lines) == 1:
					content = self.ReadOneLine(lines)


			elif self.dictionary:
				content = ast.literal_eval(lines[0])

			prefsTXT.close()

			if self.debug: print(f"Read {self.filename}")

			self.file = content
			return content

		except FileNotFoundError:
			if self.debug: print(f"File not found. Trying to create {self.filename}")
			if (callable(self.prefs)): self.CreatePrefs(self.prefs())
			else: self.CreatePrefs(self.prefs)

	def ReadOneLine(self, lines: list) -> dict:
		"""
			With a list of lines, read the first line and return it as a dictionary.

			Args:
				lines (list): The list of lines where you want to read the first one.
				
			Returns:
				A dictionary.
		"""

		result = {}        

		line = lines[0].split(self.ender)
		line.pop()
		for i in line:
			if not self.interpret:
				result[i.split(self.separator, 1)[0]] = i.split(self.separator, 1)[1]
			elif self.interpret:
				result[i.split(self.separator, 1)[0]] = ast.literal_eval(i.split(self.separator, 1)[1])        

		return result

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

		if not self.dictionary:
			text = ""
			for item in content.items():
				text += f"{item[0]}{self.separator}{item[1]}{self.ender}"

		elif self.dictionary:
			text = str(content)

		prefsTXT = open(f"{self.filename}.{self.extension}","w+")
		prefsTXT.write(text)
		prefsTXT.close()

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
