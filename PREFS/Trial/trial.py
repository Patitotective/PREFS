import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

import __init__ as PREFS

prefs = {"lang": "en", "theme": "light", "keybindings": {"Ctrl+O": "loadAudio", "Ctrl+Q": "closeApp", "Ctrl+C": "convertFile"}, "lastPath": ""}

UserPrefs = PREFS.PREFS(prefs)

