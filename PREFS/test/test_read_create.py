"""	Test dictionary parameter
"""
from pathlib import Path
import PREFS

### Test single preferences and without cascade
prefs = lambda: PREFS.read_prefs_file("prefs2.prefs")
user_prefs = PREFS.Prefs(prefs, filename="Prefs/prefs2.prefs", verbose=False)#, filterPrefs=filterPrefs) # Change (dictionary, interpret, debug) to True to test it.


def test_reading_overwrite():
	user_prefs.overwrite_prefs()
	
	assert user_prefs.read_prefs() == prefs() # Test ReadPrefs() function
	assert user_prefs.file == prefs() #Test file attribute

def test_create_prefs():
	txt = Path(user_prefs.filename).read_text()
	PREFSstr = PREFS.convert_to_prefs(prefs)

	#print(f"{txt=}\n-------\n{PREFSstr=}")

	assert txt == PREFSstr

if __name__ == "__main__":
	test_reading_overwrite()
	test_create_prefs()

	print("Everything OK")
