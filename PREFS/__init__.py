#!/usr/bin/python

#Libraries
import ast
import os

class PREFS(object):
	"""PREFS is for store user preferences, like username, theme, etcetera.
		Is very user friendly and has a few functionas that you will understand fastly, also creates a total human readable file (without any compression)"""
		
	def __init__(self, prefs: dict, filename: str="prefs", extension: str="txt", separator: str="=", ender: str="\n", 
		interpret: bool=False, dictionary: bool=False, debug: bool=False):
		
		"""
			Args:
				prefs: dict = A dictionary with the default preferences.
				filename: str (optional, "prefs" as default) = The path with the name of the file.
				extension: str (optinal, "txt" as default) = The extension of the file.
				separator: str (optional, "=" as default) = The character between the key and value in the file.
				ender: str (optional, "\n" line break as default) = The character at the end of each key:value.
				interpret: bool (optional, False as default) = Do you want to interpret the value stored, if True you could write a dictionary and read as dictioary, if False all will be returned as string.
				dictionary: bool (optional, False as default) = If True the file will be a python dictionary (avoid any error at reading), if False it will be human readble.
				debug: bool (optional, False as default) = If True print messages of all operations.
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

		self.ReadPrefs()
		
	def ReadPrefs(self):
		"""
			Try to read the prefs and if the file doesn't exist call the CreatePrefs function.

			Args:
				None

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

			return content

		except FileNotFoundError:
			if self.debug: print(f"File not found. Trying to create {self.filename}")
			if (callable(self.prefs)): self.CreatePrefs(self.prefs())
			else: self.CreatePrefs(self.prefs)

	def ReadOneLine(self, lines: list):
		"""
			With a list of lines, read the first line and return it as a dictionary.

			Args:
				lines: list = The list of lines where you want to read the first one.

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

	def CreatePrefs(self, prefs: dict):
		"""
			Creates a file with the prefs that you pass.

			Args:
				prefs: dict = The prefs that will write in the file.

			Returns:
				None
		"""
		if "/" in self.filename:
			for e, i in enumerate(self.filename.split("/")):
				if e == len(self.filename.split("/") - 1): break 
				os.mkdir(i)

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

	def WritePrefs(self, pref: str, value: any):
		"""
			Change the pref that you pass with the value that you pass, if doesn't exist, new pref.

			Args:
				pref: str = the name of the pref that you want to change, if it doesn't exist, it will create it.

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

		prefsTXT = open(f"{self.filename}","w+")
		prefsTXT.write(text)
		prefsTXT.close()

		if self.debug: print(f"Writed {pref} with {value} value in {self.filename}")

		self.ReadPrefs()

	def ReWritePrefs(self, prefs: dict = None):
		"""
			Changes the prefs with the prefs that you pass or if you don't pass nothing reset the current prefs (with the values at initializing).
			
			Args:
				prefs: dict (optional) = New prefs, if empty reset prefs.

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

			if self.debug: print(f"Writed {self.prefs} in {self.filename}")

		else: raise FileNotFoundError("Cannot write unexistent prefs")

		self.ReadPrefs()
			
	def ChangeFilename(self, filename: str):
		"""Changes the name of the file but you still has the last name when you initializing the class,
			so it won't find the file and will create it,

			Args:
				filename: str = the new name of the file.

			Returns:
				None

			"""
		if not os.path.exists(f"{self.filename}.{self.extension}"): raise FileNotFoundError("Cannot change the name of a file that doesn't exists")
		if self.debug: print(f"Trying to change {self.filename} name to {filename}")
		os.rename(self.filename+"."+self.extension, filename+"."+self.extension)
		self.filename = filename

		if self.debug: print(f"Changed filename to {self.filename}")

		# self.ReadPrefs()

	def DeleteFile(self):
		if os.path.exists(f"{self.filename}.{self.extension}"):
			if self.debug: print(f"Trying to remove {self.filename}")
			os.remove(f"{self.filename}.{self.extension}")
			if self.debug: print(f"Removed {self.filename}")
			return

		raise FileNotFoundError("Can't delete unexistent file")
