import PREFS # Importing PREFS library

prefs = {"lang": "en", "theme": "light", "lastPath": ""} # Defining default prefs
UserPrefs = PREFS.PREFS(prefs) # Creating PREFS class instance

print(UserPrefs.file) # Printing the prefs using file attribute

# print(UserPrefs.file["theme"]) # Printing theme pref

UserPrefs.WritePrefs("theme", "dark") # Changing theme pref to dark
UserPrefs.WritePrefs("lastFile", "audio.wav") # Creating lastFile pref and setting it's value to audio.Wav

print(UserPrefs.file) # Printing the prefs using file attribute
