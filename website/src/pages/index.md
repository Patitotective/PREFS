---
title: Home
description: Store and manage your preferences with PREFS.
hide_table_of_contents: true
---

import ThemedImage from '@theme/ThemedImage';
import useBaseUrl from '@docusaurus/useBaseUrl';

<ThemedImage
  alt="PREFS logo"
  sources={{
    light: useBaseUrl('/img/light_logo.png'),
    dark: useBaseUrl('/img/dark_logo.png'),
  }}
  className="center"
/>


[![Python Version](https://img.shields.io/pypi/pyversions/prefs)](https://pypi.org/project/prefs/)
[![PYPI](https://img.shields.io/pypi/v/prefs)](https://pypi.org/project/prefs/)
[![Downloads](https://pepy.tech/badge/prefs)](https://pepy.tech/project/prefs)
[![Stars](https://img.shields.io/github/stars/patitotective/prefs)](https://github.com/Patitotective/PREFS/stargazers)
[![Watchers](https://img.shields.io/github/watchers/Patitotective/PREFS)](https://github.com/Patitotective/PREFS/watchers)  
[![Build](https://img.shields.io/appveyor/build/Patitotective/PREFS)](https://ci.appveyor.com/project/Patitotective/prefs)
[![Last commit](https://img.shields.io/github/last-commit/Patitotective/PREFS)](https://github.com/Patitotective/PREFS/commits/main)
[![Size](https://img.shields.io/github/repo-size/Patitotective/PREFS)](https://github.com/Patitotective/PREFS)
[![Top languages](https://img.shields.io/github/languages/top/Patitotective/PREFS)](https://github.com/Patitotective/PREFS)
[![License MIT](https://img.shields.io/github/license/Patitotective/PREFS)](https://github.com/Patitotective/PREFS/)  
[![Made with python](https://img.shields.io/badge/made%20with-python-blue)](https://www.python.org/)

**PREFS** is a Python library to manage, store preferences and settings for your program, application or game.  
It stores a Python dictionary in a total human-readable file, you need to pass to it a default prefs that will be used when there are no preferences.

### Features
- Creates a total human-readable file.
- Supports tree/cascade in nested dictionaries.
- Supports [`export`](docs/api/prefs-class#convert_to_json)/[`import`](docs/api/functions#read_json_file) JSON files.
- Supports [`export`](docs/api/prefs-class#convert_to_yaml)/[`import`](docs/api/functions#read_yaml_file) YAML files.
- [Create a PREFS file manually and read it.](docs/api/functions#read_prefs_file).
- [Resource system to bundle PREFS files](docs/resources). 
- [Simple Command Line Interface tool](docs/api/cli).

### Limitations
- Keys can only be strings.
- The supported types are Python default ones (int, float, str, list, tuple, set, dict, etc.).

### Example
```python
import PREFS

default_prefs = {
    "theme": "light", 
    "lang": "en", 
    "keybindings": {
        "Ctrl+D": "Duplicate", 
        "Ctrl+C": "Copy", 
        "Ctr+V": "Paste", 
        "Ctrl+X": "Cut", 
        "Ctrl+Q": "Quit"
    }
}

user_prefs = PREFS.Prefs(default_prefs, filename="settings.prefs")
```
Result:
```python title="settings.prefs"
#PREFS
theme="light"
lang="en"
keybindings=>
    Ctrl+D="Duplicate"
    Ctrl+C="Copy"
    Ctrl+V="Paste"
    Ctrl+X="Cut"
    Ctrl+Q="Quit"
```
