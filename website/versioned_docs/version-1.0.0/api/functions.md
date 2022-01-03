---
id: functions
title: Functions
sidebar_position: 3
hide_title: true
---

# Functions
### `bundle()`
```py
bundle(path: str, output: str=None, alias: str=None) -> None
```

**Parameters**  
- `path (str)`: Prefs file's path.
- `output (str=None)`: Output path (by default same as `path` but appending `_resource` to the filename).
- `alias (str=None)`: An alias to reference it when reading (by default the same as the `path`).

**Returns**  
None. 

Creates a resource module (_Python_ file) with the given prefs file that you can import in a _Python_ module to get those prefs without having the prefs file itself.

:::info
This is explained at [Resources](../resources#how-to-create-a-resource-module) page.
:::

Example:
```py title="prefs.prefs"
#PREFS
lang='en'
theme=>
    background='#199396'
    font='UbuntuMono'
```
```py
import prefs

prefs.bundle("prefs.prefs")
```
```py title="prefs_resource.py"
# PREFS resource module
# Created using PREFS Python library
# https://patitotective.github.io/PREFS
# Do not modify this file
__version__ = '0.3.0'
CONTENT = {'lang': 'en', 'theme': {'background': '#199396', 'font': 'UbuntuMono'}}
ALIAS = 'prefs.prefs'
```

### `to_prefs()`
```py
to_prefs(content: dict, output: str=None) -> str
```

Converts the given dictionary into PREFS format and returns it as string, if `output` given, writes the result in that path.

**Parameters**  
- `content (dict)`: The dictionary to convert.
- `output (str)`: An output path to write the result.

**Returns**  
A string. 

:::info
Even if `output` is given, a string is still returned.
:::

Example:
```py
import prefs

content = { 
    "lang": "en", 
    "theme": {
        "background": "#199396", 
        "font": "UbuntuMono"
    }
}


string = prefs.to_prefs(content)

print(string)
>>> 
#PREFS
lang='en'
theme=>
    background='#199396'
    font='UbuntuMono'
```

:::info Info
If some directory doesn't exist in the output path it will get created.
:::

### `parse()`
```py
parse(string: str) -> dict
```
Parses a string (representing a prefs file) and returns it's content.

**Parameters**  
- `string (str)`: The string to parse.

**Returns**  
A dictionary

Example:
```py
import prefs

string = """
#PREFS
lang='en'
theme=>
    background='#199396'
    font='UbuntuMono'
"""

print(prefs.parse(string))
>>> {"lang": "en", "theme": {"background": "#199396", "font": "UbuntuMono"}}
```

### `read()`
```py
read(path: str) -> dict
```

Reads a prefs file and returns it's content.

**Parameters**  
- `path (str)`: The path to the prefs file.

**Returns**  
A dictionary.

Example:
```py title="prefs.prefs"
#PREFS
lang='en'
theme=>
    background='#199396'
    font='UbuntuMono'
```
```py
import prefs

print(prefs.read("prefs.prefs"))
>>> {"lang": "en", "theme": {"background": "#199396", "font": "UbuntuMono"}}
```

### `read_json()`
```py
read_json(path: str, **kwargs) -> dict
```
Reads a JSON file and returns it's value.

**Parameters**  
- `path (str)`: The path to the YAML file.
- `**kwargs`: This keyword arguments will be passed to the `json.load` function.

**Returns**  
A dictionary.

Example:
```py
import prefs

my_json = prefs.read_json("settings.json")
my_prefs = prefs.Prefs(my_json)
```

### `read_yaml()`
```py
read_yaml(path: str, Loader=yaml.loader.SafeLoader, **kwargs) -> dict
```
Reads a YAML file and returns it's value.

**Parameters**  
- `path (str)`: The path to the YAML file.
- `Loader=yaml.loader.SafeLoader`: YAML loader.

**Returns**  
A dictionary.

Example:
```py
import prefs

my_yaml = prefs.read_yaml("settings.yaml")
my_prefs = prefs.Prefs(my_yaml)
```
