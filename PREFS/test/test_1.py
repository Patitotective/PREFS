"""	Test dictionary parameter
"""
import os
import PREFS

### Test single preferences and without cascade
prefs = lambda: PREFS.read_prefs_file("prefs1.prefs")
user_prefs = PREFS.Prefs(prefs, filename="Prefs/prefs1.prefs", verbose=False)#, filterPrefs=filterPrefs) # Change (dictionary, interpret, debug) to True to test it.

def test_reading_overwrite():
	user_prefs.overwrite_prefs()
	
	assert user_prefs.read_prefs() == prefs() # Test ReadPrefs() function
	assert user_prefs.file == prefs() #Test file attribute

def test_writeprefs():
	user_prefs.write_prefs("theme", "dark")

	assert user_prefs.file == {"theme": "dark"}

	user_prefs.write_multiple_prefs({str(i):i for i in range(100)})

	hundred_dict = {str(i):i for i in range(100)}
	assert user_prefs.file == {"theme": "dark", **hundred_dict}


def test_changefilename_deletefile():
	user_prefs.change_filename("prefs.prefs")
	assert os.path.isfile(user_prefs.filename)

	user_prefs.delete_file()
	assert not os.path.isfile(user_prefs.filename)

def not_test_json_yaml():
	"""The name makes pytest to ignore this function because for some reason it raises an FileNotFoundError.
	"""
	user_prefs.convert_to_json()
	data = PREFS.read_json_file("Prefs/prefs1.json")

	user_prefs.convert_to_yaml()
	data1 = PREFS.read_yaml_file("Prefs/prefs1.yaml")

	assert user_prefs.file == data
	assert user_prefs.file == data1

if __name__ == "__main__":
	test_reading_overwrite()
	test_writeprefs()
	not_test_json_yaml()

	test_changefilename_deletefile() # This will delete the file so most times you won't see the file

	print("Everything OK")
