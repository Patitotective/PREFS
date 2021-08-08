"""
	Test dictionary parameter
"""

from pathlib import Path
import sys, os
import PREFS

### Test single preferences and without cascade
prefs = lambda: PREFS.read_prefs_file("prefs2")
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs2", dictionary=False, interpret=True, verbose=False, cascade=True)#, filterPrefs=filterPrefs) # Change (dictionary, interpret, debug) to True to test it.


def test_reading_overwrite():
	UserPrefs.overwrite_prefs()
	
	assert UserPrefs.read_prefs() == prefs() # Test ReadPrefs() function
	assert UserPrefs.file == prefs() #Test file attribute

def test_create_prefs():
	txt = Path(f"{UserPrefs.filename}.{UserPrefs.extension}").read_text()
	PREFSstr = PREFS.convert_to_prefs(prefs, first_line=True)
	#print("txt: ")
	#print("---------------")
	#print("PREFSstr: ")

	assert txt == PREFSstr


if __name__ == "__main__":
	test_reading_overwrite()
	test_create_prefs()

	print("Everything OK")
