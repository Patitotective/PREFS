---
id: functions
title: Functions
sidebar_position: 3
hide_title: true
---

# Functions
***

### `convert_to_prefs()`
```python
convert_to_prefs(*args, **kwargs) -> str
```

Converts the given dictionary into PREFS format and returns it as string (similar to `dump` function in `json`):

Parameters:
    `*args`: This positional arguments will be passed to the `PREFS` class.
    `**kwargs`: This keyword arguments will be passed to the `PREFS` class.

Returns:
    A string with the given dictionary in PREFS format. 

Example:
```python
import PREFS

prefs = {
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
}

prefs_repr = PREFS.convert_to_prefs(prefs) # Converting the prefs dictionary into a string in PREFS format

print(prefs_repr) # Printing prefs_repr

>>> 
#PREFS
theme='light'
lang='en'
keybindings=>
    Copy='Ctrl+C'
    Paste='Ctrl+V'
    Cut='Ctrl+X'
```
It can be used as an equivalent to `dump` function in JSON.
```py
import PREFS

prefs = {
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
}

with open("settings.prefs", "w+") as file:
    file.write(PREFS.convert_to_prefs(prefs))
```
```py title="settings.prefs"
#PREFS
theme='light'
lang='en'
keybindings=>
    Copy='Ctrl+C'
    Paste='Ctrl+V'
    Cut='Ctrl+X'
```

### `read_prefs_file()`

```python
read_prefs_file(filename: str, **kwargs) -> dict
```

Return the value of PREFS file given it's filename.

Parameters:
- `**kwargs`: This keyword arguments will be used to create a `PREFS` instance.

Returns:
	A dictionary with the PREFS of the given PREFS filename.

Example:  
If we have a file like this:
```python title="prefs.prefs"
#PREFS
theme='light'
lang='en' # Supports comments
```
We can read it this way:
```python
import PREFS

# Instead of doing this
"""
user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en"
    })
"""

user_prefs = PREFS.Prefs(PREFS.read_prefs_file("prefs.prefs"))

print(user_prefs.file)

>>> {'theme': 'light', 'lang': 'en'}
```

:::tip TIP
Remember to write quotes around all the strings.
:::

### `read_json_file()`
```python
read_json_file(filename: str, **kwargs) -> dict
```
Reads a JSON file and returns it's value.

Parameters:
- `filename (str)`: The name of JSON file to read (path).
- `**kwargs`: This keyword arguments will be passed to the `json.load` function.

Example:

```python
import PREFS

json_content = PREFS.read_json_file("filename.json") # Read filename.json" and store it's value in prefs
user_prefs = PREFS.Prefs(json_content) # Create an instance of the PREFS class using a json file as input for the prefs argument
```

### `read_yaml_file()`
```python
read_yaml_file(filename: str, **kwargs) -> dict
```
Reads a YAML file and returns it's value.

Parameters:
- `filename (str)`: The name of YAML file to read (path).

Example:

```python
import PREFS

yaml_content = PREFS.read_yaml_file("filename.yaml") # Read filename.yaml and store it's value in prefs
user_prefs = PREFS.Prefs(yaml_content) # Create an instance of the PREFS class using a yaml file as input for the prefs argument
```