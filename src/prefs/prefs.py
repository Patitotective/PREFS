import os
from typing import Dict

from .parser import parser # parser(directory).parser(module)
from .utils import check_path
from .exceptions import InvalidKeyError


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
	NESTED_TYPES = (list, set, dict, tuple)
	SUPPORTED_TYPES = (int, float, str, range, bytes, bool, type(None)) + NESTED_TYPES

	def __init__(self, prefs: Dict[str, any]=None, path: str=None):
		self.prefs = prefs
		self.path = path

		self.parser = parser.create_parser()

	@property
	def content(self) -> dict:
		return self.read()

	def get(self, key: str) -> any:
		return get_key(key, self.content, self.KEY_PATH_SEP)

	def read(self) -> dict:
		"""Read and return the prefs file's content.
		"""
		return parser.parse(path=self.path, parser=self.parser)

	def check_file(self) -> None:
		"""Creates the prefs file if it doesn't exist.
		"""
		if not os.path.isfile(self.path):
			self.create()

	def check_prefs(self, prefs: dict=None) -> dict:
		"""Checks if the given prefs (no given results in self.prefs) is a dictionary (or functions with a dictionary as return value).
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
		"""Returns the string that gets written in the prefs file.
		"""
		prefs = self.check_prefs(prefs)

		result = f"{self.FIRST_LINE}{self.ENDER_CHAR}"
		result += self.to_tree(prefs)
		
		return result

	def to_tree(self, prefs: dict, depth=0) -> str:
		"""Converts the prefs dictionary into a tree (string).
		Args:
			prefs (dict): a dictionary with the prefs to convert to text.
			depth (int=0): The indent level.
		"""	
		def check_obj(obj: object):
			"""Checks for valid object type.
			"""
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

		result = ""
		indent_char = self.INDENT_CHAR * depth

		for key, val in prefs.items():
			self.check_key(key)
			check_obj(val)

			if isinstance(val, dict) and val != {}: # To avoid writing emtpy dictionaries as nested
				result += f"{indent_char}{key}{self.SEPARATOR_CHAR}{self.CONTINUER_CHAR}{self.ENDER_CHAR}"
				result += self.to_tree(val, depth=depth + 1) # Calls itself to generate cascade/tree
				continue

			result += f"{indent_char}{key}{self.SEPARATOR_CHAR}{val!r}{self.ENDER_CHAR}"

		return result

	def create(self, prefs: dict=None) -> None:
		"""Creates a file with the given prefs (or the default ones).

		Args:
			prefs (dict): The prefs to write at self.path.
		"""
		prefs = self.check_prefs(prefs)
		check_path(self.path)

		with open(self.path, "w+") as file:			
			# If any exception is raised, remove it
			try:
				file.write(self.to_prefs(prefs))
			except Exception as error:
				os.remove(self.path)
				raise error

	def write(self, key: str, val: any) -> None:
		"""Change the value of a given key.
		To change a nested value, pass its path, e.g.: write("theme/background", "#129396")
			
		Args:
			key (str): The name of the key.
			val (any): The value to assign to the key.
		"""
		prefs = change_key(key, val, self.content, self.KEY_PATH_SEP, self.AUTO_GEN_KEYS)

		self.create(prefs) # Overwrite the file with the updated prefs

	def write_many(self, items: Dict[str, any]) -> None:
		"""Change multiple keys with the given items, this way it only opens the file once.

		Args:
			items (Dict[str, any]): The dictionary with the key:val pairs to change.
		"""		
		prefs = self.content

		for key, val in items.items():
			prefs = change_key(key, val, prefs, self.KEY_PATH_SEP, self.AUTO_GEN_KEYS)

		self.create(prefs) # Overwrite the file with the updated prefs

	def remove_key(self, key: str, *args):
		prefs = self.content
		if self.KEY_PATH_SEP in key:
			keys = key.split(self.KEY_PATH_SEP)
			dict_ = prefs[keys[0]]
			keys.pop(0)

			for e, key in enumerate(keys):
				if e == len(keys) -1:
					result = dict_.pop(key)
					continue

				dict_ = dict_[key]
		else:
			result = prefs.pop(key, *args) # Returns the removed value

		self.create(prefs)
		return result

	def overwrite(self, prefs: dict=None, key: str=None) -> None:
		"""Overwrites the key in the prefs file with the given prefs (if no key given overwrites the whole file).
			
		Args:
			prefs (dict=None): Prefs to overwrite with, by default prefs.
			key (str=None): Overwrite this key in the prefs file, by default everything.
		"""
		if not os.path.isfile(self.path):
			raise FileNotFoundError(f"Cannot overwrite nonexistent file {self.path}") # If file isn't in the path raise error

		prefs = self.check_prefs(prefs)

		if prefs is None:
			prefs = get_key(key, prefs, self.KEY_PATH_SEP)
		if key is not None:
			self.write(key, prefs)
			return

		self.create(prefs)

	def delete(self) -> None:
		"""Deletes the prefs file.
		"""
		os.remove(self.path)


class Prefs(PrefsBase): 
	"""This class creates a dictionary-like interface for PrefsBase.
	"""
	def __init__(self, prefs: (Dict[str, any], callable), path: str="prefs.prefs"):
		"""
		Args
			See PrefsBase.
		"""
		super().__init__(prefs, path)
		self.check_file()

	def __str__(self):
		"""Called when `print(self)`.
		"""
		return str(self.content)

	def __len__(self):
		return len(self.content)

	def __delitem__(self, key):
		"""Called when `del self[key]`.
		"""
		self.remove_key(key)

	def __getitem__(self, key):
		"""Called when `self[key]`.
		"""
		return super().get(key) # Calling PrefsBase.get, not Prefs.get 

	def __setitem__(self, key, val):
		"""Called when `self[key] = val`.
		"""
		self.write(key, val)

	def __contains__(self, item):
		"""Called when `item in self`.
		"""
		return item in self.content

	def __iter__(self):
		"""Called when `for i in self`.
		"""
		return iter(self.content)

	def get(self, key, *args):
		if len(args) > 1:
			raise TypeError(f"Expected one or two arguments, got {len(args)+1}")
		try:
			self.__getitem__(key)
		except KeyError as error:
			if len(args) > 0:
				return args[0]
			
			raise error

	def keys(self):
		return self.content.keys()

	def values(self):
		return self.content.values()

	def items(self):
		return self.content.items()

	def pop(self, *args):
		return self.remove_key(*args)

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


def change_key(key: str, val: any, dict_: dict, key_path_sep: str, auto_gen_keys: bool):
	if key_path_sep in key:
		return change_nested_key(
			dict_, 
			key, 
			val, 
			key_path_sep, 
			auto_gen_keys,  
		)
	
	dict_[key] = val

	return dict_

def get_key(key: str, dict_: dict, key_path_sep: str) -> any:
	if key_path_sep in key: # Means a key path ("theme/background")
		keys = key.split(key_path_sep)
		result = dict_[keys[0]]
		keys.pop(0)
		
		for i in keys:
			try:
				result = result[i]
			except KeyError:
				raise KeyError(key)

		return result

	return dict_[key]

def change_nested_key(
	dict_: dict, 
	key_path: str, 
	val: any, 
	key_path_sep: str, 
	auto_gen_keys: bool
) -> dict:
	"""Change a nested key with the given key path to the given value.

	Args:
		dict_ (dict): The dictionary to change.
		key_path (str): The path to the key, e.g.: "keybindings/Copy".
		val (any): The val to assign to the key.
		auto_gen_keys (bool=True): If some key is not found, generate it automatically.
		key_path_sep (str="/"): The character that separates nested keys.
	"""
	key_path = key_path.split(key_path_sep)
	
	if not key_path[0] in dict_ and auto_gen_keys:
		dict_[key_path[0]] = {}

	scn_dict = dict_[key_path[0]] # Set scn_dict to the first key of dict_

	key_path.pop(0)

	for e, i in enumerate(key_path):
		if e == len(key_path) - 1:
			scn_dict[i] = val
			continue

		if ((not i in scn_dict or (i in scn_dict and not isinstance(scn_dict[i], dict))) and 
			auto_gen_keys):
			scn_dict[i] = {}

		scn_dict = scn_dict[i] # Set scn_dict to scn_dict key
	
	return dict_
