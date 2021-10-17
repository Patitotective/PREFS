---
id: cli
title: Command Line Interface
sidebar_position: 1
hide_title: true
---

# Command Line Interface
**PREFS** has a simple CLI tool that you can access from your terminal right after installing **PREFS** via _Pypi_.

## Commands

### `bundle`
Bundle PREFS file into a PREFs resource to use to build your app.

_See the [usage instructions](resources.md) with a simple example._

Arguments:
- `path (positional and required)`: The path to the PREFS file to bundle.
- `-o --output (optional)`: The output path for the PREFS resource file (by default the PREFS filename plus `_resource.py`).
- `-a --alias (optional)`: The alias for the file to be used in your Python module (by default the PREFS filename itself).

Example:
```bash
PREFS bundle settings.prefs --output Resources/resource.prefs --alias preferences.prefs 
```
It will create a PREFS resource file called `resource.prefs` inside `Resources` folder that can be accesed with `preferences.prefs` alias:
```python
import PREFS

setttings = PREFS.read_prefs_file(":/preferences.prefs") # :/ and the alias
```

:::info Info
If some directory doesn't exist in the output path it creates it.
:::

### `read_prefs_file`
Given the path of a PREFS file, reads it's content and print it.

Arguments:
- `path (positional and required)`: The path to the PREFS file to bundle.
- `-i --indent_char (optional, default="\t")`: The indentation character in the PREFS file.

Example:
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
```bash
PREFS read_prefs_file settings.prefs

>>> {'theme': 'light', 'lang': 'en', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}
```

### `convert_to_prefs`
Given a dictionary as a string, prints it in PREFS format or writes the result into a file.

Arguments:
- `prefs (positional and required)`: A dictionary as a string.
- `-o --output (optional, default=None)`: The output path to write the result.
- `-i --indent_char (optional, default="\t")`: The character to indent with.

Example:
```bash
PREFS convert_to_prefs "{'theme': 'light', 'lang': 'en', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}" -o settings.prefs
```
```python title="settings.prefs"
#PREFS
theme='light'
lang='en'
keybindings=>
	Copy='Ctrl+C'
	Paste='Ctrl+V'
	Cut='Ctrl+X'
```

:::info Info
If some directory doesn't exist in the output path it creates it.
:::
