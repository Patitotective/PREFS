import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
import __init__ as PREFS

### Test multiple preferences and with cascade
prefs = {"theme": "light", "lang": "en", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}}
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs", dictionary=False, interpret=False, verbose=False, cascade=True) # Change (dictionary, interpret, debug) to True to test it.


### Test single preferences and without cascade
prefs1 = {"theme": "light"}
UserPrefs1 = PREFS.PREFS(prefs1, filename="Prefs/prefs1", dictionary=False, interpret=True, verbose=False, cascade=False)#, filterPrefs=filterPrefs) # Change (dictionary, interpret, debug) to True to test it.

def test_reading_overwrite():
	UserPrefs.OverWritePrefs()
	UserPrefs1.OverWritePrefs()
	
	assert UserPrefs1.ReadPrefs() == prefs1 # Test ReadPrefs() function
	assert UserPrefs1.file == prefs1 #Test file attribute

	assert UserPrefs.ReadPrefs() == prefs, f"{UserPrefs.ReadPrefs()} should be {prefs}" # Test ReadPrefs() function
	assert UserPrefs.file == prefs #Test file attribute

def test_writeprefs():
	UserPrefs.WritePrefs("lang", "es")
	UserPrefs1.WritePrefs("theme", "dark")

	assert UserPrefs.file == {"theme": "light", "lang": "es", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}}
	assert UserPrefs1.file == {"theme": "dark"}

def test_changefilename_deletefile():
	UserPrefs.ChangeFilename("prefs")
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == True

	UserPrefs.DeleteFile()
	assert os.path.isfile(f"{UserPrefs.filename}.{UserPrefs.extension}") == False

def test_json():
	UserPrefs.ConvertToJson()
	data = PREFS.ReadJsonFile("Prefs/prefs")

	UserPrefs1.ConvertToJson()
	data1 = PREFS.ReadJsonFile("Prefs/prefs1")

	assert UserPrefs.file == data
	assert UserPrefs1.file == data1

def test_stats():
	PREFS.GetStats()

if __name__ == "__main__":
	test_reading_overwrite()
	test_writeprefs()
	test_json()
	test_stats()

	test_changefilename_deletefile() # This will delete the file so most times you won't see the file

	print("Everything OK")
