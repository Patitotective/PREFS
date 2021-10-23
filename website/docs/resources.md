---
id: resources
title: PREFS resources
sidebar_position: 0
hide_title: true
---

# PREFS resources
***
### What are PREFS resources?
If you have ever build a _Qt_ application you may have heard of something called `QResource`, which is a resource file for your application, the application resources are in the application itself so you don't need to have those files to make your app work.  
So if you have created a PREFS file manually and you want to build your app you will need to use PREFS resources.

:::note Note
PREFS resources won't work when you build your app with _PyInstaller_, it's just a way to convert a PREFS file into a Python module.
See [PyInstaller](#PyInstaller) section to bundle your PREFS files with _PyInstaller_.
:::

### PyInstaller
To bundle your PREFS file when building your app with _PyInstaller_ you can simply add your PREFS file as a data:  
#### From `spec` file:
```py
a = Analysis(...
     datas=[('theme.prefs', '.')],
     ...
)
```
Where the first element in the tuple is the path to your PREFS file and the second the directory to write it in

Another example with the PREFS file inside a folder:
```py
a = Analysis(...
     datas=[('Prefs/theme.prefs', 'Prefs')],
     ...
)
```

:::info Info
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

:::info Info
In the command line separate the PREFS path and the destination directory with a colon `:`.
:::

:::tip More info
More info about datas in [_PyInstaller_ documentation](https://pyinstaller.readthedocs.io/en/stable/spec-files.html#adding-files-to-the-bundle).
:::

### How to create a PREFS resource file?
Lets see how you're reading your PREFS file in your Python module:
```python title="main.py"
import PREFS

theme = PREFS.read_prefs_file("theme.prefs")
print(theme)
```
Here's how `theme.prefs` looks like:
```python title="theme.prefs"
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
To bundle this PREFS file open your terminal and type:
```bash
PREFS bundle path
```
Where `path` is the path to your PREFS file, in our case `theme.prefs`.  
After running that command you should be able to see a new Python module called `theme_resource.py`. It should look like:
```py title="theme_resource.py"
# PREFS resource file
# Created using PREFS Python library
# https://patitotective.github.io/PREFS/
# Do not modify this file

VERSION = 'v0.2.65'
PREFS = {'font_family': 'UbuntuMono', 'light': {'background_color': '#dcdee0', 'font_color': '#000000', 'link_color': '#0000EE'}, 'dark': {'background_color': '#25282d', 'font_color': '#ffffff', 'link_color': '#006FEE'}}
ALIAS = 'theme.prefs'
```
You need to import that module into your Python module:
```python title="main.py"
import PREFS
import theme_resource

theme = PREFS.read_prefs_file("theme.prefs")
print(theme)
```
Then just add `:/` to the beginning of your PREFS file path (`prefs.prefs -> :/prefs.prefs`):
```py title="main.py"
import PREFS
import theme_resource

theme = PREFS.read_prefs_file(":/theme.prefs")
print(theme)
```

:::info Info
See [`bundle`'s API Reference](./api/cli#bundle) for more options. 
:::
