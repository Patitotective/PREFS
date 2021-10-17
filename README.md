# PREFS
> **PREFS is a Python library to store and manage preferences and settings.**  

[![PREFS logo](https://github.com/Patitotective/PREFS/blob/main/img/logo.png?raw=true)](https://patitotective.github.io/PREFS)

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

**PREFS** stores a Python dictionary in a total human-readable file, the PREFS file is created when it can't find it (normally the first time you run the program), otherwise if the file already exists it just read it's content.

## Installation:
On windows:
`pip install PREFS`

On MacOS and Linux:
`pip3 install PREFS`

### Syntax:

Each PREFS file is an instance of the `PREFS` class:  
The `PREFS` class has one required parameter, which is a dictionary with the default preferences (used to create the file when it can't it).

```Python
default_prefs = {
  "theme": "light", 
  "lang": "en", 
  "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}
}

user_prefs = PREFS.Prefs(default_prefs)
```

This code will create a file like this:
```python
#PREFS
theme='light'
lang='en'
keybindings=>
  Ctrl+C='Copy'
  Ctrl+V='Paste'
  Ctrl+X='Cut'
```
A total human readable file that supports cascade/tree in nested dictionaries.

## Other functions
- `read_json_file()`.
- `read_yaml_file()`.
- `read_prefs_file()`.
- `convert_to_prefs()`.

## Documentation
PREFS documentation can be found at https://patitotective.github.io/PREFS/docs/ with more examples and information.

[Extra info](https://github.com/Patitotective/PREFS/blob/main/EXTRAINFO.md).

About
---

- GitHub page: https://github.com/Patitotective/PREFS.
- Pypi page: https://pypi.org/project/PREFS/.

- Contact me:
  - Discord: **Patitotective#0127**.
  - Email: **cristobalriaga@gmail.com**.

***v0.2.56***
