# src/exceptions.py


class InvalidPath(Exception):
	"""This exception is raised when a given path is not valid.
	"""
	pass


class InvalidKeyError(Exception):
	"""This error is raised when a key is not valid.
	"""
	pass


class InvalidResourceAlias(Exception): 
	"""This error will be raised when a PREFS resource is not valid.
	"""
	pass


class DeprecationWarning(Warning):
	"""Overwriting default DeprecationWarning, otherwise warn doesn't work.
	"""
	pass
