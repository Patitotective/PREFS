---
title: Home
description: Store and manage preferences easily.
hide_table_of_contents: true
---
import {useLatestVersion} from '@theme/hooks/useDocs';

[![PREFS logo](https://github.com/Patitotective/PREFS/blob/develop/assets/logo.png?raw=true)](https://patitotective.github.io/PREFS)

[![Supported Python versions](https://img.shields.io/pypi/pyversions/prefs)](https://pypi.org/project/prefs/)
[![PREFS version](https://img.shields.io/pypi/v/prefs)](https://pypi.org/project/prefs/)
[![Downloads](https://pepy.tech/badge/prefs)](https://pepy.tech/project/prefs)
[![Stars](https://img.shields.io/github/stars/patitotective/prefs)](https://github.com/Patitotective/PREFS/stargazers)
[![Watchers](https://img.shields.io/github/watchers/Patitotective/PREFS)](https://github.com/Patitotective/PREFS/watchers)

[![Build](https://img.shields.io/appveyor/build/Patitotective/PREFS)](https://ci.appveyor.com/project/Patitotective/prefs)
[![Last commit](https://img.shields.io/github/last-commit/Patitotective/PREFS)](https://github.com/Patitotective/PREFS/commits/main)
![Size](https://img.shields.io/github/repo-size/Patitotective/PREFS)
[![License MIT](https://img.shields.io/github/license/Patitotective/PREFS)](https://github.com/Patitotective/PREFS/)  

[![Made with Python](https://img.shields.io/badge/made%20with-python-blue)](https://www.python.org/)
[![Discord server](https://img.shields.io/discord/891409914533118012?logo=discord)](https://discord.gg/as85Q4GnR6)

**PREFS** is Python library that stores preferences in a text file with a dictionary-like structure.

### Features
- Simple syntax.
- Supports tree/cascade in nested dictionaries.
- Supports [`export`](docs/api/prefs#to_json)/[`import`](docs/api/functions#read_json) JSON files.
- Supports [`export`](docs/api/prefs#to_yaml)/[`import`](docs/api/functions#read_yaml) YAML files.
- Supports bytes and ranges.
- [Create a PREFS file manually and read it.](docs/api/functions#read).
- [Resource system to bundle PREFS files](docs/resources). 
- [Simple Command Line Interface tool](docs/api/cli).

### Limitations
- Keys can only be strings.
- The supported types are int, float, str, list, tuple, set, dict, **bytes** and **ranges**.

### Example
```py
import prefs

default_prefs = {
    "lang": "en", 
    "theme": "dark", 
    "scheme": {
        "background-color": "#AB2E6A", 
        "font": {
            "color": "#129396", 
            "size": 15
            "family": "UbuntuMono"
        }
    }
}

my_prefs = prefs.Prefs(default_prefs, path="settings.prefs")
print(my_prefs["scheme/font/size"])
>>> 15

my_prefs["scheme/font/size"] = 20
my_prefs.pop("theme")
```
A new file got created that looks like:
```py title="settings.prefs"
#PREFS
lang='en'
scheme=>
    background-color='#AB2E6A'
    font=>
        color='#129396'
        size=20
        family='UbuntuMono'
```

<bold>v{useLatestVersion().label}</bold>
