---
id: cli
title: Command Line Interface
sidebar_position: 1
hide_title: true
---

# Command Line Interface
_PREFS_ has a simple CLI tool that you can access from your terminal right after installing _PREFS_ via _Pypi_.

## Commands
### `bundle`
Bundle PREFS file into a PREFs resource to use to build your app.

:::info
See an usage example [here](../resources#how-to-create-a-resource-module).
:::

```
Usage: prefs bundle [OPTIONS] PATH

  Bundle a PREFS file into a Python module

Options:
  -o, --output TEXT  The output path
  -a, --alias TEXT   The alias to be referenced as the path
  --help             Show this message and exit.
```
Example:
```bash
prefs bundle theme.prefs --output resources/theme.py 
```
It will create a (_PREFS_) resource module file called `theme.py` inside the `resources` directory:
```py
import prefs
from resources import theme

theme_data = PREFS.read(":/theme.prefs") # :/ and the alias
```
(To better understand the above example read [this](../resources#how-to-create-a-resource-module)).

:::info Info
If some directory doesn't exist in the output path it creates it.
:::

### `read`
Given the path of a PREFS file, reads it's content and print it.

```
Usage: prefs read [OPTIONS] PATH

  Reads a PREFS file and displays its content as a Python dictionary

Options:
  --help  Show this message and exit.
```

Example:
```py title="settings.prefs"
#PREFS
lang='en'
theme=>
    background='#199396'
    font='UbuntuMono'
```
```bash
prefs read settings.prefs

>>> {"lang": "en", "theme": {"background": "#199396", "font": "UbuntuMono"}}
```

### `about`
```
Usage: prefs about [OPTIONS]                                                              

  Shows information about PREFS                             

Options:                                         
  --help  Show this message and exit.   
```
