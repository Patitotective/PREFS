import PREFS

prefs = {"theme": "light", "lang": "en"} # Defining default prefs
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs") # Creating PREFS instance to create prefs file

UserPrefs.OverWritePrefs() # Overwriting the prefs with the default prefs

print(UserPrefs.ReadPrefs()) # Printing the prefs

UserPrefs.WritePrefs("theme", "dark") # Changing the theme pref from light to dark

print(UserPrefs.ReadPrefs()) # Printing the prefs again
