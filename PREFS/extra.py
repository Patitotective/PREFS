import os
import sys

def check_path(path: str):
	"""Check if a path exists, if some directory is missing it creates it.
	"""
	if not os.path.isdir(os.path.split(path)[0]) and os.sep in path: # Check that the required path doesn't exist and there is a slash in it
		directories_list = split_path(os.path.split(path)[0]) # Get all directories to the file
		directories_list = accumulate_list(directories_list, separator=os.sep) # Accumulate them ["home", "cristobal"] -> ["home", "home/cristobal"]
		
		for directory in directories_list: # Iterate trough each directory on the path
			if not os.path.isdir(directory): # If the directory doesn't exist
				os.mkdir(directory) # Create it

def split_path(path: str) -> list:
	result = os.path.normpath(path)
	return path.split(os.sep)

def accumulate_list(my_list: (list, tuple), separator: str="") -> list:
	"""["a", "b", "c"] -> ["a", "ab", "abc"]
	"""
	result = []
	
	for e, ele in enumerate(my_list):
		if e == 0:
			result.append(ele)
			continue

		result.append(f"{result[e-1]}{separator}{ele}")

	return result

def remove_comments(string: str, comment_char: str="#") -> str:
	"""Remove comments from strings.

	Note:
		Iterates through the given string, if founds a quote and there isn't a backslash \ before it set in_string to True, if finds a # and in_string is False break the loop and cut the string until there and return it.
	Args:
		string (str): An string to remove the comments from
		comment_char: (str, optional="#"): Which character represents a comment

	Returns:
		The same string without comments.

	"""

	in_string = False # If iterating in string ignore comments otherwise don't 
	quote = "" # Type of quote (simple or double), because you can't open a string with simple quotes and close it with double

	for e, char in enumerate(string): # Iterate thorught the string
		if char == "'" or char == '"': # Checks if the current character is a quote
			if e != 0: # Checks if the quote isn't in the first place
				if string[e -1] == "\\": # Checks if the character before it is a backslahs
					continue # If it is ignore it

			if quote == char or not in_string: # If the type of quote is the current char, or if isn't in a string
				quote = char # Set the quote to the char
				in_string =  not in_string # And set in_string to True if False and viceversa

		if char == comment_char and not in_string: # If the current character is the comment character and isn't in a string
			string = string[:e] # Cut string until here
			break # And break

	return string # Return the string

def get_built_file_path(filename: str) -> str:
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    bundle_path = os.path.abspath(os.path.join(bundle_dir, filename))			

    # This is just the base folder concatenated to the filename, it means there is no built file
    normal_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), filename))

    return bundle_path if bundle_path != normal_path else None

