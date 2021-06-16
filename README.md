<p align="center">
  <a href="https://github.com/Patitotective/PREFS/wiki" target="blank">
  <img src="logo1.png" alt="PREFS logo" /></a>
</p>

## Why?
**PREFS's purpose is to facilitate the process of store information, user information (that won't get lost when the program ends).**

## Installation:
On windows:
```pip install PREFS```

On Mac and Linux:
```pip3 install PREFS```

### Store Prefs:
PREFS writes dictionaries as human readable files and converts it into dictionaries at read time.
Creates a .txt file in dictionary structure, your will see something like this:
```
firstEntry="02/05/2021"
theme="Dark"
username="Patitotective"
age="21"
```

### Syntaxis:
First you have to create an instance of the class PREFS (each class is a new file):
```
UserPrefs = PREFS.PREFS(prefs = {"firstEntry": today, username": "Patitotective", "theme": "Dark", "age": 21})
```
from this you can call two main methods:

```ReadPrefs()```: Returns a dictionary with your prefs.

```WritePrefs()```: Requires two arguments, first the name of the pref that you want to change (if pref exists) or create it if it doesn't, and second the value that will replace the old value.


## Documentation
PREFS documentation can be found at https://github.com/Patitotective/PREFS/wiki with more examples and information.
