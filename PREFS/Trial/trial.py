import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

import __init__ as PREFS

# Converting prefs dictionary into PREFS format
prefs = {
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    }

PREFSrepresentation = PREFS.convert_to_prefs(prefs)

print(PREFSrepresentation)
