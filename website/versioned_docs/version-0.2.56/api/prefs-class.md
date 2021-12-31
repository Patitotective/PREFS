---
id: prefs-class
title: Prefs class
sidebar_position: 2
hide_title: true
---

# Prefs class
---

## Init
- `prefs (dict)`: A dictionary or a function that returns a dictionary as the default PREFS.
- `filename (str=prefs.prefs)`: The filename of the PREFS file.
- `verbose (bool=False)`: Pritn debug messages of all operations.
- `indent_char (str="\t")`: The character to indent with.
- `auto_generate_keys (bool=True)`: Auto generate the required keys when key path (see [`write_prefs()`](#write_prefs)).

## Attributes
Ignoring the init attributes.

### `file`
Easier way to access to the PREFS file. Equivalent to [`read_prefs()`](#read_prefs).  
Example:

```python
import PREFS

default_prefs = {
    "theme": "light",
    "lang": "en"
}
user_prefs = PREFS.Prefs(default_prefs)

print(user_prefs.file)

>>> {'theme': 'light', 'lang': 'en'}
```

## Methods

### `read_prefs()`
```python
read_prefs() -> dict
```

Reads the PREFS file and returns it's value.

Parameters: Doesn't require any arguments.  
Returns: A dictionary reading the PREFS file.

Example:

```python
import PREFS

user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    })


print(user_prefs.read_prefs())

>>> {'theme': 'light', 'lang': 'en'}
```

### `write_prefs()`
```python
write_prefs(pref: str, value: any) -> None
```

Reads the PREFS file and changes the given key to the given value.

Parameters:

- `pref (str)`: The name of the pref to modify or create if it doesn't exist.
- `value (any)`: The value to assign to the given pref.

Returns: `None`.

Example:

```python
import PREFS

user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    }) # Creating an PREFS instance

print(user_prefs.file["lang"]) # Getting the lang value from the PREFS and printing it
>>> en

user_prefs.write_prefs("lang", "es") # Changing the lang value from en to es

print(user_prefs.file["lang"]) # Getting the lang value from the PREFS and printing it
>>> es
```

To change the value of a nested dictionary pass a path of keys to find the value you want.
Example:

```python
import PREFS

user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    }) # Creating an PREFS instance

print(user_prefs.file["keybindings"]) # Getting the keybindings value (which is a dictionary) from the PREFS and printing it
>>> {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}

user_prefs.write_prefs("keybindings/Copy", "Ctrl+D") # Changing the Copy value inside the dictionary keybindings inside the PREFS file from Ctrl+C to Ctrl+D

print(user_prefs.file["keybindings"]) # Getting the keybindings value (which is a dictionary) from the PREFS and printing it
>>> {'Copy': 'Ctrl+D', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}
```

Another example creating a new pref in a nested dictionary:

```python
import PREFS

user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    }) # Creating an PREFS instance

print(user_prefs.file["keybindings"]) # Getting the keybindings value (which is a dictionary) from the PREFS and printing it
>>> {'Copy': 'Ctrl+D', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}

user_prefs.write_prefs("keybindings/Quit", "Ctrl+Q") # Creating the Quit pref inside keybindings dictionary inside the PREFS file with Ctrl+Q as value

print(user_prefs.file["keybindings"]) # Getting the keybindings value (which is a dictionary) from the PREFS and printing it
>>> {'Copy': 'Ctrl+D', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X', 'Quit': 'Ctrl+Q'}
```

### `write_multiple_prefs()`
```python
write_multiple_prefs(prefs: Dict[str, any]) -> None
```

To efficiently write multiple prefs at once.

Parameters:
- `prefs (Dict[str, any])`: A dictionary with the prefs to change.

Returns: `None`.

For example:
```python
print(user_prefs.file) # Getting the lang value from the PREFS and printing it
>>> {'theme': 'light', 'lang': 'en', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}

user_prefs.write_multiple_prefs({"theme": "dark", "lang": "es"}) # Changing the lang value from en to es

print(user_prefs.file) # Getting the lang value from the PREFS and printing it
>>> {'theme': 'dark', 'lang': 'es', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}
```
It is super useful when you need to change huge prefs because it changes all those prefs at once, otherwise it will need to open the file, write the pref, close it and repeat.

### `overwrite_prefs()`
```python
overwrite_prefs(prefs: dict=None) -> None
```

Overwrites the PREFS file with the default PREFS, if passed dictionary in prefs parameter overwrites PREFS file with these.

Parameters:
- `prefs (dict, optional=None)`: A dictionary to overwrites the PREFS file with, if passed `None` overwrites PREFS file with default PREFS.

Returns: `None`.

Example:

```python
import PREFS

user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    }) # Creating an PREFS instance


user_prefs.overwrite_prefs() # Overwriting the PREFS file with the default PREFS

print(user_prefs.file) # Getting PREFS with file attribute and printing it

>>> {'theme': 'light', 'lang': 'en', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}

user_prefs.write_prefs("lang", "es") # Changing the lang value from en to es

print(user_prefs.file) # Getting PREFS with file attribute and printing it

>>> {'theme': 'light', 'lang': 'es', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}

```

The first time we run the above example the program will do this:

- Define an instance of the PREFS class and pass a default PREFS
- Overwrite the PREFS file with the default ones.
- Print the PREFS file
- Change the `lang` pref from en to es
- Print again the PREFS file.

The second time will do this:

- Define an instance of the PREFS class and pass a default PREFS
- Overwrite the PREFS file that contains the modified `lang` pref with the default PREFS.

So the program will always has the same output because we overwrite the old PREFS with the default PREFS.

### `change_filename()`
```python
change_filename(filename: str) -> None
```

This function will change the name of the PREFS file if it exists.

:::note Note
It will be useless if you don't change the filename parameter manually because when you run your code again **PREFS** will search for a file with old filename.
:::

Parameters:
- `filename (str)`: The new filename of the PREFS file.

Returns: `None`.

Example:

```python
import PREFS

user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    }) # Creating an PREFS instance

user_prefs.change_filename("other_filename.prefs") # Changing the name of the PREFS file from prefs to otherFilename

```

### `delete_file()`
```python
delete_file() -> None
```

Deletes the PREFS file if it exists.

Parameters: `None`.
Returns: `None`.

Example:

```python
import PREFS

user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    }) # Creating an PREFS instance

user_prefs.delete_file() # Delete the PREFS file

```

### `convert_to_json()`
```python
convert_to_json(filename: str="", extension: str="json", **kwargs) -> None
```

Converts the PREFS file into a JSON file.

Parameters:

- `filename (str, optional="")`: The name of the JSON file, if empty the same name of the PREFS file.
- `extension (str, optional="json")`: The extension of the JSON file, json as default.
- `**kwargs`: This kwargs will be passed to `json.load` function, in case you want certain configuration to load the JSON file  


Returns: `None`.

Example:

```python
import PREFS

user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    }) # Creating an PREFS instance

user_prefs.convert_to_json() # Coverts the PREFS file into a JSON one

```

### `convert_to_yaml()`
```python
convert_to_yaml(filename: str="", extension: str="yaml", Loader=yaml.loader.SafeLoader, **kwargs) -> None
```

Converts the PREFS file into a YAML file.

Parameters:

- `filename (str, optional="")`: The name of the YAML file, if empty the same name of the PREFS file.
- `extension (str, optional="yaml")`: The extension of the YAML file, yaml as default.
- `Loader (optional=yaml.loader.SafeLoader)`: YAML loader for `yaml.load` function.
- `**kwargs`: This kwargs will be passed to `yaml.load` function, in case you want certain configuration to load the YAML file  

Returns: `None`.

Example:

```python
import PREFS

user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    }) # Creating an PREFS instance

user_prefs.convert_to_yaml() # Coverts the PREFS file into a YAML one

```
