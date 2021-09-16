"""
	Test dictionary parameter
"""

import sys, os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join('..')))
import __init__ as PREFS

### Test single preferences and without cascade
prefs = lambda: PREFS.read_prefs_file("prefs2.prefs")
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs2.prefs", interpret=True, verbose=False, cascade=True)#, filterPrefs=filterPrefs) # Change (dictionary, interpret, debug) to True to test it.


def test_reading_overwrite():
	UserPrefs.overwrite_prefs()
	
	assert UserPrefs.read_prefs() == prefs() # Test ReadPrefs() function
	assert UserPrefs.file == prefs() #Test file attribute

def test_create_prefs():
	txt = Path(UserPrefs.filename).read_text()
	PREFSstr = PREFS.convert_to_prefs(prefs)

	#print(f"{txt=}\n-------\n{PREFSstr=}")

	assert txt == PREFSstr

if __name__ == "__main__":
	test_reading_overwrite()
	test_create_prefs()

	print("Everything OK")
