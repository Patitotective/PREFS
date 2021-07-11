import PREFS # Importing PREFS library

prefs = {"lang": "en", 
	"theme": "light", 
	"keybindings": {"Ctrl+O": "loadAudio", "Ctrl+Q": "closeApp", "Ctrl+C": "convertFile"}, 
	"lastPath": ""} # Defining default prefs

UserPrefs = PREFS.PREFS(prefs) # Creating PREFS instance to create prefs file

print(UserPrefs.file) # Printing the prefs

print(UserPrefs.file["theme"]) # Printing certain using file attribute

UserPrefs.WritePrefs("theme", "dark") # Changing the theme pref from light to dark

print(UserPrefs.file) # Printing the prefs again

UserPrefs.WritePrefs("lastFile", "audio.wav") # Creating new pref

print(UserPrefs.file) # Printing the prefs again

UserPrefs.WritePrefs("keybindings/Ctrl+Q", "Alt+F4")

print(UserPrefs.file) # Printing the prefs again
