class InvalidKeyError(Exception):
	"""This error is raised when a key is not valid.
	"""
	pass


class InvalidResourceError(Exception): 
	"""This error will be raised when a PREFS resource is not valid.
	"""
	pass


class DeprecationWarning(Warning):
	"""Overwriting default DeprecationWarning, otherwise warn doesn't work.
	"""
	pass
