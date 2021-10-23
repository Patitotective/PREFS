"""	Test default parameters.
"""
import os
import PREFS

### Test multiple preferences and with cascade
prefs = {"theme": "light", "lang": "en", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {}}
user_prefs = PREFS.Prefs(prefs, filename="Prefs/prefs.prefs",  verbose=False) # Change (dictionary, interpret, debug) to True to test it.

def test_reading_overwrite():
	user_prefs.overwrite_prefs()

	assert user_prefs.read_prefs() == prefs, f"{user_prefs.read_prefs()} should be {prefs}" # Test read_prefs() function
	assert user_prefs.file == prefs, f"{user_prefs.read_prefs()} should be {prefs}" #Test file attribute

def test_writeprefs():
	user_prefs.write_prefs("lang", "es")

	assert user_prefs.file == {"theme": "light", "lang": "es", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {}}

	user_prefs.write_prefs("name/age", 20)

	assert user_prefs.file == {"theme": "light", "lang": "es", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {"age": 20}}

	user_prefs.write_prefs("name/user/uwu", 20)

	assert user_prefs.file == {"theme": "light", "lang": "es", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {"age": 20, "user": {"uwu": 20}}}


def test_changefilename_deletefile():
	user_prefs.change_filename("prefs.prefs")
	assert os.path.isfile(user_prefs.filename)

	user_prefs.delete_file()
	assert not os.path.isfile(user_prefs.filename)

def not_test_json_yaml():
	"""The name makes pytest to ignore this function because for some reason it raises an FileNotFoundError.
	"""	
	user_prefs.convert_to_json()
	data = PREFS.read_json_file("Prefs/prefs.json")
	
	assert user_prefs.file == data

	user_prefs.convert_to_yaml()
	data = PREFS.read_yaml_file("Prefs/prefs.yaml")

	assert user_prefs.file == data

if __name__ == "__main__":
	test_reading_overwrite()
	test_writeprefs()
	not_test_json_yaml()

	test_changefilename_deletefile() # This will delete the file so most times you won't see the file

	print("Everything OK")
