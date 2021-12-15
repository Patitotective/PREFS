import os
import sys

def check_path(path: str):
	"""Check if a path exists, if some directory is missing it creates it.
	"""
	if os.path.exists(path):
		return

	dir_list = split_path(os.path.split(path)[0]) # Remove the filename if there is one and split the directories
	path = dir_list[0]

	for e, dir_ in enumerate(dir_list):
		if os.path.ismount(dir_): # On Windows C:\ and / on Linux
			continue

		if e > 0:
			path = os.path.join(path, dir_) # os.path.join("trial", "sub") -> "trial/sub" (on Windows "trial\sub")

		if not os.path.isdir(path):
			os.mkdir(path)

def split_path(path: str):
	path = os.path.normpath(path) # Remove redundant separators (A//B, A/B/, A/./B and A/foo/../B become A/B)
	# path = os.path.normcase(path) # https://docs.python.org/3/library/os.path.html#os.path.normcase
	path = os.path.expanduser(path) # Convert "~" into the home user directory
	path = path.split(os.sep)
	
	if path[0] == "": # For unix systems
		path[0] = "/" # Add mount point if it got removed when spliting the path
	elif path[0].lower() == "c:":
		path[0] = "C:\\"

	return path

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

if __name__ == "__main__":	
	# Tests
	# path = "C:/Users/crist/Documents/Projects/PREFS/src/trial/sub1/test.prefs" # Windows
	# path = "/home/cristobal/Documents/Projects/PREFS/src/trial/sub2/test.prefs" # Linux
	# path = "~/Documents/Projects/PREFS/src/trial/sub3/trial.pres" # Both
	path = "trial/sub4/test.prefs" # Both

	# print(split_path(path))
	check_path(path)
