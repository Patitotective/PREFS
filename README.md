<p align="center">
  <a href="https://prefs.readthedocs.io/en/latest/" target="blank">
  <img src="logo1.png" alt="PREFS Logo" /></a>
</p>

## Why?
_PREFS's purpose is to facilitate the process of store information, user information (that won't get lost when you close the program)._

## Installation:
On windows:
```pip install PREFS```

On Mac and Linux:
```pip3 install PREFS```

Also if you want to see the code you can download `__init__.py`, i sometimes forgot to upload the code, so for get the latest version check https://pypi.org/project/PREFS/.

## Store Prefs
The main feature is to store preferences, read and write them.
It creates a .txt file where in a dictionary like structure, your prefs will be stored, i.e.:
```
firstEntry="02/05/2021"
theme="Dark"
username="Patitotective"
age="21"
```

### Syntaxis:
Each prefs file is an instace of PREFS class, first you have to create an instance of the class PREFS:
```
UserPrefs = PREFS.PREFS(prefs = {"age": 21, "username": "Patitotective"})
```
from this you could call the two methods:

```ReadPrefs()```: It will return a dictionary with your prefs (key and value).

```WritePrefs()```: It requires two arguments, first the name of the pref that you want to change (if pref exists) or create it if it doesn't.


## Documentation

PREFS documentation can be found at [PREFS DOCUMENTATION](https://github.com/Patitotective/PREFS/wiki) with more examples and information.
