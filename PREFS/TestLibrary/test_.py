"""
	Test default parameters.
"""

import sys, os
import PREFS

### Test multiple preferences and with cascade
prefs = {"theme": "light", "lang": "en", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {}}
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs", dictionary=False, interpret=True, verbose=False, cascade=True) # Change (dictionary, interpret, debug) to True to test it.

def test_reading_overwrite():
	UserPrefs.overwrite_prefs()

	assert UserPrefs.read_prefs() == prefs, f"{UserPrefs.read_prefs()} should be {prefs}" # Test read_prefs() function
	assert UserPrefs.file == prefs, f"{UserPrefs.read_prefs()} should be {prefs}" #Test file attribute

def test_writeprefs():
	UserPrefs.write_prefs("lang", "es")

	assert UserPrefs.file == {"theme": "light", "lang": "es", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {}}

	UserPrefs.write_prefs("name/age", 20)

	assert UserPrefs.file == {"theme": "light", "lang": "es", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {"age": 20}}


def test_changefilename_deletefile():
	UserPrefs.change_filename("prefs")
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == True

	UserPrefs.delete_file()
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == False

def test_json():
	UserPrefs.convert_to_json()
	data = PREFS.read_json_file("Prefs/prefs")

	assert UserPrefs.file == data

if __name__ == "__main__":
	test_reading_overwrite()
	test_writeprefs()
	test_json()

	test_changefilename_deletefile() # This will delete the file so most times you won't see the file

	print("Everything OK")
