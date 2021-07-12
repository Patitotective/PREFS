import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

import __init__ as PREFS

"""UserPrefs = PREFS.PREFS(prefs = {
    "theme": "light",
    "lang": "en"
    })

UserPrefs.OverWritePrefs()

print(UserPrefs.file)

UserPrefs.WritePrefs("lang", "es")
 
print(UserPrefs.file)
"""

PREFS.GetStats()
