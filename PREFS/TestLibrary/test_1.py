"""
	Test dictionary parameter
"""

import sys, os
import PREFS

### Test single preferences and without cascade
prefs = lambda: PREFS.read_prefs_file("prefs1")
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs1", dictionary=True, interpret=True, verbose=False, cascade=True)#, filterPrefs=filterPrefs) # Change (dictionary, interpret, debug) to True to test it.

def test_reading_overwrite():
	UserPrefs.overwrite_prefs()
	
	assert UserPrefs.read_prefs() == prefs() # Test ReadPrefs() function
	assert UserPrefs.file == prefs() #Test file attribute

def test_writeprefs():
	UserPrefs.write_prefs("theme", "dark")

	assert UserPrefs.file == {"theme": "dark"}

def test_changefilename_deletefile():
	UserPrefs.change_filename("prefs")
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == True

	UserPrefs.delete_file()
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == False

def test_json_yaml():
	UserPrefs.convert_to_json()
	data = PREFS.read_json_file(filename="Prefs/prefs1", extension="json")

	UserPrefs.convert_to_yaml()
	data1 = PREFS.read_yaml_file("Prefs/prefs1")

	assert UserPrefs.file == data
	assert UserPrefs.file == data1

if __name__ == "__main__":
	test_reading_overwrite()
	test_writeprefs()
	test_json_yaml()

	test_changefilename_deletefile() # This will delete the file so most times you won't see the file

	print("Everything OK")
