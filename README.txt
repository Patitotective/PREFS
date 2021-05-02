Why?

PREFS's purpose is to facilitate the process of store information, like prefs or user information (that don't will lost when program ends).
-------------------------------------------------------------------------------------------------------------------------------------------
Store Prefs:

The main (and unique) feature is store prefs, read them and also (re)write.
It creates a .txt file where, like dictionary structure, your prefs will be stored, like this:
firstEntry="02/05/2021"
theme="Dark"
username="Patitotective"
age="21"
-------------------------------------------------------------------------------------------------------------------------------------------
Syntaxis:

First you have to create an instance of the class PREFS:
UserPrefs = PREFS.PREFS(prefs = {"age": 21, "username": "Patitotective"})

from this you could call the two methods:
ReadPrefs(): It will return a dictionarie with your prefs (key and value).
WritePrefs(): It requires two arguments, first the name of the pref that you want to change (if pref exists) or create it doesn't (like a dictionarie).
