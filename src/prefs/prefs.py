# Libraries
import os
import json
import yaml
from typing import Dict

# Dependencies
from .utils import check_path, change_nested_key
from .exceptions import InvalidKeyError
from .parser import parser  # parser(folder).parser(module)


class PrefsBase:
	FIRST_LINE = "#PREFS"
	SEPARATOR_CHAR = "="
	ENDER_CHAR = "\n"
	CONTINUER_CHAR = ">"
	COMMENT_CHAR = "#"
	INDENT_CHAR = "\t"
	KEY_PATH_SEP = "/"
	INVALID_KEY_CHARS = (SEPARATOR_CHAR, CONTINUER_CHAR, KEY_PATH_SEP)
	AUTO_GEN_KEYS = True
	SUPPORTED_TYPES = (int, float, str, list, set, dict, tuple, range, bytes, bool, type(None))

	def __init__(self, prefs: Dict[str, any]=None, path: str=None):
		self.prefs = prefs
		self.path = path

		self.parser = parser.create_parser()

	@property
	def content(self) -> dict:
		return self.read()

	def read(self) -> dict:
		"""Reads the prefs file.
	
		Returns:
			The prefs.
		"""
		prefs = parser.parse(path=self.path, parser=self.parser)

		return prefs # Return prefs file as dictionary

	def check_file(self) -> None:
		"""Creates the prefs file if it doesn't exist.
		"""
		if not os.path.isfile(self.path):
			self.create()

	def check_prefs(self, prefs: dict=None) -> dict:
		"""Checks if self.prefs or the given prefs are callable and if they're dictionaries.
		"""
		if prefs is None:
			prefs = self.prefs

		if callable(prefs):
			prefs = prefs()

		if not isinstance(prefs, dict):
			raise TypeError(
				f"self.prefs must be a dictionary or a function with a dictionary as return value, given {type(prefs).__name__}"
			)

		return prefs

	def check_key(self, key: str) -> None:
		if not isinstance(key, str):
			raise InvalidKeyError(f"Invalid key {key!r}. Keys can only be strings, given {type(key).__name__} type")

		if any([inv_char in key for inv_char in self.INVALID_KEY_CHARS]):
			raise InvalidKeyError(f"Invalid key {key!r}. A key cannot include the following characters {self.INVALID_KEY_CHARS}")

	def to_prefs(self, prefs: dict=None) -> str:
		"""Returns the string gets written in the prefs file.
		"""
		prefs = self.check_prefs(prefs)

		result = f"{self.FIRST_LINE}{self.ENDER_CHAR}"
		result += self.to_tree(prefs)
		
		return result

	def to_tree(self, prefs: dict, depth=0) -> str:
		"""Converts the prefs dictionary a tree (string).

			Args:
				prefs (dict): a dictionary with the prefs to convert to text.
				depth (int=0): The depth level (to indent).

			Returns:
				A string with the prefs, ready to write.
		"""	
		def check_obj(obj: object):
			if type(obj) not in self.SUPPORTED_TYPES:
				raise TypeError(f"Unsupported {type(obj).__name__!r} type at {key!r} key, supported types are {[i.__name__ for i in self.SUPPORTED_TYPES]}")
		
			if isinstance(obj, (list, tuple, set)):
				for i in obj:
					check_obj(i)
			elif isinstance(obj, dict):
				for k, v in obj.items():
					self.check_key(k)
					check_obj(v)

		prefs = self.check_prefs(prefs)

		result = "" # String to append each pref:value combination
		indent_char = self.INDENT_CHAR * depth # Multiply depth by a tabulation, e.i.: if depth 0 no tabulation.

		for key, val in prefs.items(): # Iterate through prefs dictionary items
			self.check_key(key)
			check_obj(val)

			if isinstance(val, dict) and val != {}: # If values is a dictionary and cascade is True and isn't an empty dictionary
				result += f"{indent_char}{key}{self.SEPARATOR_CHAR}{self.CONTINUER_CHAR}{self.ENDER_CHAR}"
				result += self.to_tree(val, depth=depth + 1) # Calls itself to generate cascade/tree
				continue

			result += f"{indent_char}{key}{self.SEPARATOR_CHAR}{val!r}{self.ENDER_CHAR}" # Write key:value (str) with quotes

		return result

	def create(self, prefs: dict=None) -> None:
		"""Creates a file with the given prefs.

			Args:
				prefs (dict): The prefs to write in self.path.
		"""
		prefs = self.check_prefs(prefs)
		check_path(self.path)

		# Both do the same thing
		# Open a file, and if any exception is raised, remove it
		"""
		try:
			file = open(self.path, "w+")
			file.write(self.to_prefs(prefs))
		except Exception as error:
			os.remove(self.path)
			raise error
		finally:
			file.close()
		"""
		with open(self.path, "w+") as file:			
			try:
				file.write(self.to_prefs(prefs))
			except Exception as error:
				os.remove(self.path)
				raise error
		# """

	def write(self, key: str, val: any) -> None:
		"""Change content key to the given value.
			To change nested key value, pass its path, e.g.: write(key="keybindings/Copy", val="ctrl+c")
			
			Args:
				key (str): The name of the key to change or create.
				val (any): The value of the key.
		"""
		prefs = self.content
		
		if self.KEY_PATH_SEP in key:
			prefs = change_nested_key(prefs, key, val, auto_gen_keys=self.AUTO_GEN_KEYS, key_path_sep=self.KEY_PATH_SEP)
		else:
			prefs[key] = val

		self.create(prefs) # Overwrite file

	def write_many(self, items: Dict[str, any]) -> None:
		"""Change multiple prefs with the given items, this way it only opens the file once.
			
		Args:
			items (Dict[str, any]): The dictionary with the key:val pairs to change.
		"""		
		prefs = self.content

		for key, val in items.items():
			if self.KEY_PATH_SEP in key:
				prefs = change_nested_key(prefs, key, val, auto_gen_keys=self.AUTO_GEN_KEYS, key_path_sep=self.KEY_PATH_SEP)
			else:
				prefs[key] = val

		self.create(prefs) # Overwrite file

	def remove_key(self, key: str, *args):
		prefs = self.content
		result = prefs.pop(key, *args)

		self.create(prefs)
		return result

	def overwrite(self, prefs: dict=None, key: str=None) -> None:
		"""Overwrites the key in the prefs file with the given prefs.
			
			Args:
				prefs (dict=None): Prefs to overwrite with, by default prefs.
				key (str=None): Overwrite this key in the prefs file, by default everything.
		"""
		if not os.path.isfile(self.path):
			raise FileNotFoundError(f"Cannot overwrite nonexistent file {self.path}") # If file isn't in the path raise error

		prefs = self.check_prefs(prefs)
		
		if key is not None:
			prefs[key] = self.prefs[key]

		self.create(prefs)

	def delete(self) -> None:
		"""Deletes the prefs file.
		"""
		if not os.path.isfile(self.path):
			raise FileNotFoundError(f"Cannot delete nonexistent file ({self.path})")
		
		os.remove(self.path)
		
	def to_json(self, path: str=None, **kwargs) -> None:
		"""Converts the prefs file into a json file.
		
		Args:
			path (str=None): If no path given, prefs file with .json as extension.
		"""
		if path is None:
			path = f"{os.path.splitext(self.path)[0]}.json"

		with open(path, "w+") as file:
			json.dump(self.content, file, **kwargs)

	def to_yaml(self, path: str=None, **kwargs) -> None:
		"""Converts the prefs file into a yaml file.
		
		Args:
			path (str=None): If no path given, prefs file with .yaml as extension.
		"""
		if path is None:
			path = f"{os.path.splitext(self.path)[0]}.yaml"

		with open(path, "w+") as file:
			yaml.dump(self.content, file, **kwargs)


class Prefs(PrefsBase): 
	"""This class creates a dictionary-like interface for PrefsBase.
	"""
	def __init__(self, prefs: Dict[str, any], path: str="prefs.prefs"):
		"""
		Args
			See PrefsBase.
		"""
		super().__init__(prefs, path)

		self.check_file()

	def __str__(self):
		return str(self.content)

	# FIXIT Print prefs differently when repr
	def __repr__(self):
		return f"<{type(self).__name__!r} {self.content} at {self.path!r}>"

	def __len__(self):
		return len(self.content)

	def __delitem__(self, key):
		self.remove_key(key)

	def __getitem__(self, key):
		return self.content[key]

	def __setitem__(self, key, value):
		self.write(key, value)

	def __contains__(self, item):
		return item in self.content

	def __iter__(self):
		return iter(self.content)

	def keys(self):
		return self.content.keys()

	def values(self):
		return self.content.values()

	def items(self):
		return self.content.items()

	def pop(self, *args):
		return self.remove_key(*args)

	def get(self, *args):
		return self.content.get(*args)

	def has_key(self, key: str):
		return key in self.content

	def clear(self):
		prefs = self.content
		result = prefs.clear()
		self.create(prefs)
		return result

	def update(self, *args):
		prefs = self.content
		result = prefs.update(*args)
		self.create(prefs)
		return result

	def popitem(self):
		prefs = self.content
		result = prefs.popitem()
		self.create(prefs)
		return result
