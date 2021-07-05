![PREFS logo](https://github.com/Patitotective/PREFS/blob/main/Images/logo1.png?raw=true)

![Python Version](https://img.shields.io/pypi/pyversions/prefs)
[![PYPI](https://img.shields.io/pypi/v/prefs)](https://pypi.org/project/prefs/)
[![Downloads](https://pepy.tech/badge/prefs)](https://pepy.tech/project/prefs)

## Why?

**PREFS's purpose is to facilitate the process of store information, user information (that won't get lost when the program ends).**

## Installation:

On windows:
`pip install PREFS`

On Mac and Linux:
`pip3 install PREFS`

### Store Prefs:

PREFS writes dictionaries as human readable files and converts it into dictionaries at read time.
Creates a .txt file in dictionary structure, your will see something like this:

```Python
firstEntry="02/05/2021"
theme="Dark"
username="Patitotective"
age="21"
```

### Syntaxis:

First you have to create an instance of the class PREFS (each class is a new file):

```Python
UserPrefs = PREFS.PREFS(prefs = {"firstEntry": today, "username": "Patitotective", "theme": "Dark", "age": 21})
```

The most important parameter is prefs, which is a dictionary with your default preferences. That means the preferences that all users will has just opening your application or game.

from this you can call two main methods:

`ReadPrefs()`: Returns a dictionary with your prefs.

`WritePrefs()`: Requires two arguments, first the name of the pref that you want to change (if pref exists) or create it if it doesn't, and second the value that will replace the old value.

## Documentation

PREFS documentation can be found at https://github.com/Patitotective/PREFS/wiki with more examples and information.
