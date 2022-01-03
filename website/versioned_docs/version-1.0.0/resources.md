---
id: resources
title: PREFS resources
sidebar_position: 0
hide_title: true
---

# PREFS resources
### What are PREFS resources?
_PREFS_ resources are made to convert (bundle) a prefs file into a _Python_ module.

:::note
This was originally made for _PyInstaller_, but it didn't work, so they're now an extra feature.
:::

### PyInstaller
To use your prefs files in an application built with _PyInstaller_ you can simply add your PREFS file as a data:  

#### From the `.spec` file:
```py
a = Analysis(...
     datas=[('theme.prefs', '.')],
     ...
)
```
Where the first element in the tuple is the path to your prefs file and the second the directory to write it in

Another example with the prefs file inside a folder:
```py
a = Analysis(...
     datas=[('Prefs/theme.prefs', 'Prefs')],
     ...
)
```

:::info
A dot `.` means the current directory.
:::

#### From the command line:
```bash
pyinstaller --add-data 'theme.prefs:.' myscript.py
```
Another example with the PREFS file inside a folder:
```bash
pyinstaller --add-data 'Prefs/theme.prefs:Prefs' myscript.py
```

:::info
In the command line separate the prefs path and the destination directory with a colon `:`.
:::

:::tip More info
More info about datas in [_PyInstaller_ documentation](https://pyinstaller.readthedocs.io/en/stable/spec-files.html#adding-files-to-the-bundle).
:::

### How to create a resource module?
Lets see how you're reading your prefs file in your Python script:
```py title="main.py"
import prefs

theme = prefs.read("theme.prefs")
```

Where `theme.prefs` looks like:
```py title="theme.prefs"
#PREFS
font_family="UbuntuMono"
light=>
	background_color="#dcdee0"
	font_color="#000000"
	link_color="#0000EE"
dark=>
	background_color="#25282d"
	font_color="#ffffff"
	link_color="#006FEE"
```
To bundle this prefs file open your terminal and type:
```bash
prefs bundle theme.prefs
```
:::info
This can also be achieved by using the [`bundle` function](./api/functions#bundle).
:::

Where `theme.prefs` is the path to your PREFS file. 

After running that command you should be able to see a new Python file called `theme_resource.py`.  
It should look like:
```py title="theme_resource.py"
# PREFS resource module
# Created using PREFS Python library
# https://patitotective.github.io/PREFS
# Do not modify this file
__version__ = '0.3.0'
CONTENT = {'font_family': 'UbuntuMono', 'light': {'background_color': '#dcdee0', 'font_color': '#000000', 'link_color': '#0000EE'}, 'dark': {'background_color': '#25282d', 'font_color': '#ffffff', 'link_color': '#006FEE'}}
ALIAS = 'prefs.prefs'
```
You need to import that module into your Python script:
```py title="main.py"
import prefs
import theme_resource

theme = prefs.read("theme.prefs")
```
Then just add `:/` to the beginning of your PREFS file path (`theme.prefs -> :/theme.prefs`).  
Now you can remove `theme.prefs`, because `theme_resource.py` is enough.
```py title="main.py"
import prefs
import theme_resource

theme = prefs.read(":/theme.prefs")
print(theme)
>>> {'font_family': 'UbuntuMono', 'light': {'background_color': '#dcdee0', 'font_color': '#000000', 'link_color': '#0000EE'}, 'dark': {'background_color': '#25282d', 'font_color': '#ffffff', 'link_color': '#006FEE'}}
```
