# PREFS
> **Store and manage preferences easily.**  

[![PREFS logo](https://github.com/Patitotective/PREFS/blob/main/assets/logo.png?raw=true)](https://patitotective.github.io/PREFS)

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

## Installation
On _Windows_:  
`pip install PREFS`

On _MacOS_ and _Linux_:  
`pip3 install PREFS`

### Getting started
To initialize your preferences you will need to instance the `Prefs` class with the first argument as the default preferences (the ones used the first time the program runs or whenever the file gets deleted).

```py
import prefs

default_prefs = {
  "lang": "en", 
  "theme": {
    "background": "#ffffff", 
    "font": "UbuntuMono", 
  }, 
}

my_prefs = prefs.Prefs(default_prefs)
```

The above code will create a file called `prefs.prefs` that looks like:
```py
#PREFS
lang='en'
theme=>
  background='#ffffff' 
  font='UbuntuMono'
```
Then you can change values as if it were a dictionary.
```py
my_prefs["lang"] = "es"
```
And now `prefs.prefs` will look like:
```py
#PREFS
lang='es'
theme=>
  background='#ffffff'
  font='UbuntuMono'
```

You can write your own _PREFS_ files manually as well, to manage your application's color scheme or the translations.

***

## About
- Docs: https://patitotective.github.io/PREFS/docs/start.
- GitHub: https://github.com/Patitotective/PREFS.
- Pypi: https://pypi.org/project/PREFS/.
- Discord: https://discord.gg/as85Q4GnR6.

Contact me:
- Discord: **Patitotective#0127**.
- Tiwtter: [@patitotective](https://twitter.com/patitotective).
- Email: **cristobalriaga@gmail.com**.

***v1.0.0***
