"""
	Test default parameters.
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
import __init__ as PREFS

### Test multiple preferences and with cascade
prefs = {"theme": "light", "lang": "en", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {}}
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs", dictionary=False, interpret=True, verbose=False, cascade=True) # Change (dictionary, interpret, debug) to True to test it.

def test_reading_overwrite():
	UserPrefs.OverWritePrefs()

	assert UserPrefs.ReadPrefs() == prefs, f"{UserPrefs.ReadPrefs()} should be {prefs}" # Test ReadPrefs() function
	assert UserPrefs.file == prefs, f"{UserPrefs.ReadPrefs()} should be {prefs}" #Test file attribute

def test_writeprefs():
	UserPrefs.WritePrefs("lang", "es")

	assert UserPrefs.file == {"theme": "light", "lang": "es", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {}}

	UserPrefs.WritePrefs("name/age", 20)

	assert UserPrefs.file == {"theme": "light", "lang": "es", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}, "name": {"age": 20}}


def test_changefilename_deletefile():
	UserPrefs.ChangeFilename("prefs")
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == True

	UserPrefs.DeleteFile()
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == False

def test_json():
	UserPrefs.ConvertToJson()
	data = PREFS.ReadJsonFile("Prefs/prefs")

	assert UserPrefs.file == data

if __name__ == "__main__":
	test_reading_overwrite()
	test_writeprefs()
	test_json()

	test_changefilename_deletefile() # This will delete the file so most times you won't see the file

	print("Everything OK")
