"""
	Test dictionary parameter
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
import __init__ as PREFS

### Test single preferences and without cascade
prefs = lambda: PREFS.ReadPREFSFile("prefs1")
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs1", dictionary=True, interpret=True, verbose=False, cascade=True)#, filterPrefs=filterPrefs) # Change (dictionary, interpret, debug) to True to test it.

def test_reading_overwrite():
	UserPrefs.OverWritePrefs()
	
	assert UserPrefs.ReadPrefs() == prefs() # Test ReadPrefs() function
	assert UserPrefs.file == prefs() #Test file attribute

def test_writeprefs():
	UserPrefs.WritePrefs("theme", "dark")

	assert UserPrefs.file == {"theme": "dark"}

def test_changefilename_deletefile():
	UserPrefs.ChangeFilename("prefs")
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == True

	UserPrefs.DeleteFile()
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == False

def test_json():
	UserPrefs.ConvertToJson()
	data = PREFS.ReadJsonFile("Prefs/prefs1")

	assert UserPrefs.file == data

if __name__ == "__main__":
	test_reading_overwrite()
	test_writeprefs()
	test_json()

	test_changefilename_deletefile() # This will delete the file so most times you won't see the file

	print("Everything OK")
