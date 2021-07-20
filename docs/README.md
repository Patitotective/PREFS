<a id="user-content-prefs" class="anchor" aria-hidden="true" href="#prefs">
 
<div align="center">
  <img src="https://github.com/Patitotective/PREFS/blob/main/Images/logo1.png?raw=true" alt="PREFS logo">
</div>

</a>

[![Python Version](https://img.shields.io/pypi/pyversions/prefs)](https://pypi.org/project/prefs/)
[![PYPI](https://img.shields.io/pypi/v/prefs)](https://pypi.org/project/prefs/)
[![Downloads](https://pepy.tech/badge/prefs)](https://pepy.tech/project/prefs)
[![Stars](https://img.shields.io/github/stars/patitotective/prefs)](https://github.com/Patitotective/PREFS/stargazers)
[![Watchers](https://img.shields.io/github/watchers/Patitotective/PREFS)](https://github.com/Patitotective/PREFS/watchers)
<br/>
[![Build](https://img.shields.io/appveyor/build/Patitotective/PREFS)](https://ci.appveyor.com/project/Patitotective/prefs)
[![Last commit](https://img.shields.io/github/last-commit/Patitotective/PREFS)](https://github.com/Patitotective/PREFS/commits/main)
[![Size](https://img.shields.io/github/repo-size/Patitotective/PREFS)](https://github.com/Patitotective/PREFS)
[![Top languages](https://img.shields.io/github/languages/top/Patitotective/PREFS)](https://github.com/Patitotective/PREFS)
[![License MIT](https://img.shields.io/github/license/Patitotective/PREFS)](https://github.com/Patitotective/PREFS/)
<br/>
[![made-with-python](https://img.shields.io/badge/made%20with-python-blue)](https://www.python.org/)

## What is PREFS?

**PREFS is a Python library that facilitate the process of store and manage user preferences, simple but useful.**

### How does PREFS work?
In a nutshell what PREFS does is search for a PREFS file with the given name and if not found create it with the default PREFS.

## Installation:

On windows:
`pip install PREFS`

On MacOS and Linux:
`pip3 install PREFS`

### Syntax:

Each PREFS file is an instance of the PREFS class:  
PREFS class has one required parameter, which is a dictionary with the default preferences, default means the preferences that all users will have at first time.

```Python
UserPrefs = PREFS.PREFS(prefs = {
  "theme": "light", 
  "lang": "en", 
  "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}
})
```

This code will create a file like this:

```python
#PREFS
theme=light
lang=en
keybindings=>
  Ctrl+C=Copy
  Ctrl+V=Paste
  Ctrl+X=Cut
```

A total human readable file that supports cascade/tree in nested dictionaries.

---

The main methods to manage the preferences are are:

- `ReadPrefs()`: Returns a dictionary reading the PREFS file.

- `WritePrefs()`: Requires two arguments, first the name of the pref that you want to change (if pref exists) or create if it doesn't, and second argument is the value that you want to assign to the pref. If using nested dictionaries pass in key parameter the keys path separated by a forward slash, e.g.: 
`WritePrefs("keybindings/Ctr+C", "Ctrl+D")`

- `ConvertToJson()`: Converts the PREFS file into a json one.

Methods outside PREFS class:

- `ReadJsonFile()`: Requires a the filename of the json file to read and returns it's value.

- `ReadPREFSFile()`: Given the filename of a PREFS file reads it and returns it's value.

## Documentation

PREFS documentation can be found at https://prefs-documentation.readthedocs.io with more examples and information.

---

## Links

- GitHub page: https://github.com/Patitotective/PREFS.
- Pypi page: https://pypi.org/project/PREFS/.

- Contact me:
  - Discord: **patitotective#0127**.
  - Email: **cristobalriaga@gmail.com**.



**v0.1.7**
