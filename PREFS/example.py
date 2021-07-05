import PREFS

prefs = {"theme": "light", "lang": "en"}
UserPrefs = PREFS.PREFS(prefs, filename="Prefs/prefs")

print(UserPrefs.ReadPrefs())
