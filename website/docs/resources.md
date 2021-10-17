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

VERSION = 'v0.2.56'
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
Then just add `:/` to the begining of your PREFS file path (`prefs.prefs -> :/prefs.prefs`):
```py title="main.py"
import PREFS
import theme_resource

theme = PREFS.read_prefs_file(":/theme.prefs")
print(theme)
```
Noy you can build your app without any issue.

:::info Info
See [`bundle`'s API Reference](./api/cli) for more options. 
:::
