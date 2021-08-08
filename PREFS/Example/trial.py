import PREFS # Importing PREFS library

prefs = {"lang": "en", 
	"theme": "light", 
	"keybindings": {"Ctrl+O": "loadAudio", "Ctrl+Q": "closeApp", "Ctrl+C": "convertFile"}, 
	"lastPath": ""} # Defining default prefs

result = PREFS.convert_to_prefs(prefs) # Creating PREFS instance to create prefs file
print(result)
