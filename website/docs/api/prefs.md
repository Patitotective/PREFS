---
id: prefs
title: Prefs class
sidebar_position: 2
hide_title: true
---

# `Prefs` class
This class provides a dictionary-like inteface for the `PrefsBase` class.

:::note
`PrefsBase` is not documented but it's included here with the `Prefs` class
:::

## Example
```py
import prefs

default_prefs = { 
    "lang": "en", 
    "theme": {
        "background": "#199396", 
        "font": "UbuntuMono"
    }
}

my_prefs = prefs.Prefs(default_prefs)

my_prefs["lang"] = "es"
print(default_prefs)
>>> 
{ 
    "lang": "es", 
    "theme": {
        "background": "#199396", 
        "font": "UbuntuMono"
    }
}

# Acess to nested keys
my_prefs["theme/background"] = "#953e68"
print(default_prefs)
>>> 
{ 
    "lang": "es", 
    "theme": {
        "background": "#953e68", 
        "font": "UbuntuMono"
    }
}

# Remove keys
my_prefs.pop("lang")
print(default_prefs)
>>> 
{ 
    "theme": {
        "background": "#953e68", 
        "font": "UbuntuMono"
    }
}
```

The supported dictionary methods are:
```py
__str__# print(my_prefs)
__repr__ # repr(my_prefs)
__len__ # len(my_prefs)
__delitem__ # del my_prefs[item]
__getitem__ # my_prefs[item]
__setitem__ # my_prefs[key] = val
__contains__ # key in my_prefs
__iter__ # for i in my_prefs
keys
values
items
pop
get
has_key
clear
update
popitem
```

## Init
- `prefs (Dict[str, any], callable)`: A dictionary or a function that returns a dictionary to use as the default preferences.
- `path (str="prefs.prefs")`: The path of the _PREFS_ file.

:::info
The default preferences are the ones ued the first time the program runs or whenever the files gets deleted.  
If any directory in the path doesn't exist, it will get created.
:::

## Class Attributes
```py
FIRST_LINE = "#PREFS"
SEPARATOR_CHAR = "="
ENDER_CHAR = "\n"
CONTINUER_CHAR = ">"
COMMENT_CHAR = "#"
INDENT_CHAR = "\t"
KEY_PATH_SEP = "/"
INVALID_KEY_CHARS = (SEPARATOR_CHAR, CONTINUER_CHAR, KEY_PATH_SEP)
AUTO_GEN_KEYS = True
SUPPORTED_TYPES = (int, float, str, list, set, dict, tuple, range, bytes, bool, NoneType)
```

## Properties
### `content`
Access the prefs file's content (by calling [`read`](#read) method).  
Example:

```py
import prefs

default_prefs = {
    "theme": "light",
    "lang": "en"
}

my_prefs = prefs.Prefs(default_prefs)

print(prefs.content)
>>> {'theme': 'light', 'lang': 'en'}
```

## Methods
### `read()`
```py
read() -> dict
```

Reads the prefs file and returns it's content.

Parameters: doesn't require any arguments.  
Returns: a dictionary.

Example:
```py
import prefs

my_prefs = prefs.Prefs({ 
        "lang": "en", 
        "theme": {
            "background": "#199396", 
            "font": "UbuntuMono"
        }
    }
)


print(my_prefs.read())

>>> {'lang': 'en', 'theme': {'background': '#199396', 'font': 'UbuntuMono'}}
```

### `write()`
```py
write(key: str, val: any) -> None
```

Changes the given key to the given value and updates the prefs file.

Parameters:
- `key (str)`: The key to change.
- `val (any)`: The value to assign.

Returns: `None`.

Example:
```py
import prefs

my_prefs = prefs.Prefs({ 
        "lang": "en", 
        "theme": {
            "background": "#199396", 
            "font": "UbuntuMono"
        }
    }
)

print(my_prefs["lang"])
>>> en

my_prefs.write("lang", "es")

print(my_prefs["lang"])
>>> es
```

To change the value of a nested key, you need to give it a path of keys to find the value you want.
Example:
```py
import prefs

my_prefs = prefs.Prefs({ 
        "lang": "en", 
        "theme": {
            "background": "#199396", 
            "font": "UbuntuMono"
        }
    }
)

print(my_prefs["theme"])
>>> {'background': '#199396', 'font': 'UbuntuMono'}

my_prefs.write("theme/background", "#953e68")

print(my_prefs["theme"])
>>> {'background': '#953e68', 'font': 'UbuntuMono'}
```

### `write_many()`
```py
write_many(items: Dict[str, any]) -> None
```

To efficiently write multiple prefs at once (by opening the file just once).

Parameters:
- `items (Dict[str, any])`: A dictionary with the prefs to change.

Returns: `None`.

Example:
```py
import prefs

my_prefs = prefs.Prefs({ 
        "lang": "en", 
        "theme": {
            "background": "#199396", 
            "font": "UbuntuMono"
        }
    }
)

my_prefs.write_many({"theme/background": "#953e68", "theme/font": "AllerDisplay"})

print(my_prefs["theme"])
>>> 
"theme": {
    "background": "#953e68", 
    "font": "AllerDisplay"
}
```

### `overwrite()`
```py
overwrite(prefs: dict=None, key: str=None) -> None
```

Overwrites the prefs file with the default prefs or with the given prefs.
If the `key` parameter is given, overwrite that key.

Parameters:
- `prefs (dict=None)`: A dictionary to overwrites the prefs with.
- `key (str=None)`: A key to overwrite.

Returns: `None`.

Example:
```py
import prefs

my_prefs = prefs.Prefs({ 
        "lang": "en", 
        "theme": {
            "background": "#199396", 
            "font": "UbuntuMono"
        }
    }
)

my_prefs["lang"] = "es"

print(my_prefs["lang"])
>>> 'es'

my_prefs.overwrite(key="lang") # If key is not given, it will overwrite the whole prefs

print(my_prefs["lang"])
>>> 'en' # The default value
```

### `delete()`
```py
delete() -> None
```

Deletes the prefs file.

Parameters: `None`.
Returns: `None`.

Example:

```py
import prefs

my_prefs = prefs.Prefs({ 
        "lang": "en", 
        "theme": {
            "background": "#199396", 
            "font": "UbuntuMono"
        }
    }
)

my_prefs.delete()
print(my_prefs["lang"])
```
The above code will raise a `FileNotFoundError` since the prefs file got deleted.
If we remove the line where we delete the prefs file and run the code again, it will work, because _PREFS_ creates the prefs file at init if it is not found.

:::note
If you want to create the prefs file again after deleting it without rerunning the program, you can do:
```py
my_prefs.create() # Not documented
```
:::

### `to_json()`
```py
to_json(self, path: str=None, **kwargs) -> None
```

Converts the prefs file into a JSON file.

Parameters:
- `path (str=None)`: The output path, by default the [`path`](#init) with the `.json` extension.
- `**kwargs`: This keyword arguments will be passed to `json.dump` function, in case you want certain configuration.

Returns: `None`.

Example:
```py
import prefs

my_prefs = prefs.Prefs({ 
        "lang": "en", 
        "theme": {
            "background": "#199396", 
            "font": "UbuntuMono"
        }
    }
)

my_prefs.to_json()
```

```json title="prefs.json"
{"lang": "en", "theme": {"background": "#199396", "font": "UbuntuMono"}}
```

### `to_yaml()`
```py
to_yaml(self, path: str=None, **kwargs) -> None
```

Converts the prefs file into a YAML file.

Parameters:
- `path (str=None)`: The output path, by default the [`path`](#init) with the `.json` extension.
- `**kwargs`: This keyword arguments will be passed to `yaml.dump` function, in case you want certain configuration.

Returns: `None`.

Example:
```py
import prefs

my_prefs = prefs.Prefs({ 
        "lang": "en", 
        "theme": {
            "background": "#199396", 
            "font": "UbuntuMono"
        }
    }
)

my_prefs.to_yaml()
```

```yaml title="prefs.yaml"
lang: en
theme:
  background: '#199396'
  font: UbuntuMono
```
