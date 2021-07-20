"""
	Test dictionary parameter
"""

import sys, os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join('..')))
import __init__ as PREFS

### Test single preferences and without cascade
prefs = lambda: PREFS.ReadPREFSFile("prefs2")
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs2", dictionary=False, interpret=True, verbose=False, cascade=True)#, filterPrefs=filterPrefs) # Change (dictionary, interpret, debug) to True to test it.


def test_reading_overwrite():
	UserPrefs.OverWritePrefs()
	
	assert UserPrefs.ReadPrefs() == prefs() # Test ReadPrefs() function
	assert UserPrefs.file == prefs() #Test file attribute

def test_create_prefs():
	txt = Path(f"{UserPrefs.filename}.{UserPrefs.extension}").read_text()
	PREFSstr = PREFS.ConvertToPREFS(prefs)
	#print("txt: ")
	#print(txt)
	#print("---------------")
	#print("PREFSstr: ")
	#print(PREFSstr)

	assert txt == PREFSstr


if __name__ == "__main__":
	test_reading_overwrite()
	test_create_prefs()

	#test_changefilename_deletefile() # This will delete the file so most times you won't see the file

	print("Everything OK")
