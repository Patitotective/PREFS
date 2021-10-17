---
id: start
title: Getting started
description: Learn how to get started with PREFS
sidebar_position: 0
hide_title: true
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import {useLatestVersion, useActiveVersion} from '@theme/hooks/useDocs';

# Getting started

## Installation and import

To install PREFS you need to have pip installed (if you don't have it installed see [Pypi installation](https://pip.pypa.io/en/stable/installation/)):

<Tabs groupId="operating-systems">
<TabItem value="windows" label="Windows" default>

```bash
pip install PREFS
```        
:::tip TIP
<span>If you want to install {useActiveVersion().label === 'Next' ? 'some version' : useActiveVersion().label} and not the latest use: </span><code>pip install PREFS={useActiveVersion().label === 'Next' ? 'versionNumber' : useActiveVersion().label}</code>.  
Or if you already have PREFS and you want to upgrade it use <code>pip install PREFS --upgrade</code> (and look at the <a href='https://patitotective.github.io./'>latest version of the documentation</a>).
:::


</TabItem>
<TabItem value="linux" label="Linux and MacOs">

```bash
pip3 install PREFS
```
:::tip TIP
<span>If you want to install {useActiveVersion().label === 'Next' ? 'some version' : useActiveVersion().label} and not the latest use </span><code>pip3 install PREFS={useActiveVersion().label === 'Next' ? 'versionNumber' : useActiveVersion().label}</code>.  
Or if you already have PREFS and you want to upgrade it use <code>pip3 install PREFS --upgrade</code> (and look at the <a href='https://patitotective.github.io./'>latest version of the documentation</a>).
:::

</TabItem>
</Tabs>

Once you have installed PREFS correctly create a new python file and import PREFS:
```python
import PREFS
```

## Create PREFS
To create a PREFS file you need to create an instance of the PREFS class passing in the `prefs` parameter a dictionary with the default PREFS (default the used when it can't find the PREFS file):

```python
user_prefs = PREFS.Prefs(prefs={
    "theme": "light",
    "lang": "en",
    "keybindings": {"Copy": "Ctrl+C", "Paste": "Ctrl+V", "Cut": "Ctrl+X"}
    })
```

You can change the PREFS filename by changing [`filename`](./api/prefs-class#init) parameter, which supports path.

If you open your PREFS file (by default `prefs.prefs`), you will see something like this:

```python
#PREFS
theme='light'
lang='en'
keybindings=>
    Copy='Ctrl+C'
    Paste='Ctrl+V'
    Cut='Ctrl+X'
```

## Read PREFS
To access to your PREFS file you can call the [`read_prefs()`](./api/prefs-class/#read_prefs) method or access to the [`file`](./api/prefs-class/#file) attribute, both returns a dictionary with your PREFS:

Using `read_prefs()` method:

```python
print(user_prefs.read_prefs()) # Getting PREFS with read_prefs() method and printing it

>>> {'theme': 'light', 'lang': 'en', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}
```

Using `file` attribute:

```python
print(user_prefs.file) # Getting PREFS with file attribute and printing it

>>> {'theme': 'light', 'lang': 'en', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}
```

## Write PREFS
To change the value of a pref you need to use [`write_prefs()`](./api/prefs-class/#write_prefs) method which requires:

-   `pref (str)`: The name of the pref to modify or create if it doesn't exist.
-   `value (any)`: The value to assign to the given pref.

For example:

```python
print(user_prefs.file["lang"]) # Getting the lang value from the PREFS and printing it
>>> en

user_prefs.write_prefs("lang", "es") # Changing the lang value from en to es

print(user_prefs.file["lang"]) # Getting the lang value from the PREFS and printing it
>>> es
```

If you want to change the value of a nested dictionary you need to pass the keys path separated by a forward slash.
In this case we will change the value of `"Copy"` which is inside `"keybindings"` so our path should `"keybindings/Copy"`:   

```python
print(user_prefs.file["keybindings"]) # Getting the keybindings value (which is a dictionary) from the PREFS and printing it
>>> {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}

user_prefs.write_prefs("keybindings/Copy", "Ctrl+D") # Changing the Copy value inside the dictionary keybindings inside the PREFS file from Ctrl+C to Ctrl+D

print(user_prefs.file["keybindings"]) # Getting the keybindings value (which is a dictionary) from the PREFS and printing it
>>> {'Copy': 'Ctrl+D', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}
```

In the above example we have accessed to a nested dictionary using the keys path and modified the pref `"Copy"` from `Ctrl+C` to `Ctrl+D`.

As you know a PREFS file is like a Python dictionary so if you pass any key that isn't in the PREFS file it will be created:
For example:

```python
print(user_prefs.file["keybindings"]) # Getting the keybindings value (which is a dictionary) from the PREFS and printing it
>>> {'Copy': 'Ctrl+D', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}

user_prefs.write_prefs("keybindings/Quit", "Ctrl+Q") # Creating the Quit pref inside keybindings dictionary inside the PREFS file with Ctrl+Q as value

print(user_prefs.file["keybindings"]) # Getting the keybindings value (which is a dictionary) from the PREFS and printing it
>>> {'Copy': 'Ctrl+D', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X', 'Quit': 'Ctrl+Q'}
```

## Write multiple PREFS
To efficiently write multiple prefs at once use [`write_multiple_prefs()`](./api/prefs-class/#write_multiple_prefs):

Parameters:
- `prefs (Dict[str, any])`: A dictionary with the prefs to change.

For example:
```python
print(user_prefs.file) # Getting the lang value from the PREFS and printing it
>>> {'theme': 'light', 'lang': 'en', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}

user_prefs.write_multiple_prefs({"theme": "dark", "lang": "es"}) # Changing the lang value from en to es

print(user_prefs.file) # Getting the lang value from the PREFS and printing it
>>> {'theme': 'dark', 'lang': 'es', 'keybindings': {'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Cut': 'Ctrl+X'}}
```
It is super useful when you need to change huge prefs because it changes all those prefs at once, otherwise it will need to open the file, write the pref, close it and repeat.
