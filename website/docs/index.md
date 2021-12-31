---
id: start
title: Getting started
sidebar_position: 0
hide_title: true
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import {useLatestVersion, useActiveVersion} from '@theme/hooks/useDocs';

# Getting started
## Installation
To install PREFS you need to have pip installed (if you don't have it installed see [Pypi installation](https://pip.pypa.io/en/stable/installation/)):

<Tabs groupId="operating-systems">
<TabItem value="windows" label="Windows" default>

```bash
pip install prefs
```        
:::tip
<span>If you want to install {useActiveVersion().label === 'Next' ? 'some version' : useActiveVersion().label} and not the latest use </span><code>pip install prefs={useActiveVersion().label === 'Next' ? 'versionNumber' : useActiveVersion().label}</code>.  
Or if you already have PREFS and you want to upgrade it use <code>pip install prefs --upgrade</code> (and look at the <a href='https://patitotective.github.io./'>latest version of the documentation</a>).
:::

</TabItem>
<TabItem value="linux" label="Linux and MacOs">

```bash
pip3 install prefs
```

:::tip
<span>If you want to install {useActiveVersion().label === 'Next' ? 'some version' : useActiveVersion().label} and not the latest use </span><code>pip3 install prefs={useActiveVersion().label === 'Next' ? 'versionNumber' : useActiveVersion().label}</code>.  
Or if you already have PREFS and you want to upgrade it use <code>pip3 install prefs --upgrade</code> (and look at the <a href='https://patitotective.github.io./'>latest version of the documentation</a>).
:::

</TabItem>
</Tabs>

Once you have installed PREFS correctly create a new _Python_ file and import prefs:
```py
import prefs
```

## Creating
To create a prefs file you will need to instance the `Prefs` class with the first argument as the default preferences.

:::info
The default preferences are the ones used the first time the program runs or whenever the file gets deleted.
:::

```py
import prefs

default_prefs = {
    "lang": "en", 
    "theme": "dark", 
    "scheme": {
        "background": "#AB2E6A", 
        "font-color": "#129396", 
        "font": "UbuntuMono"
    }
}

my_prefs = prefs.Prefs(default_prefs)
```

The above code will create a file that looks like:
```py title="prefs.prefs"
#PREFS
lang='en'
theme='dark'
scheme=>
    background='#AB2E6A'
    font-color='#129396'
    font='UbuntuMono'
```
You can change the file's path with the [`path`](./api/prefs#init) parameter.

:::info
If any directory in the `path` doesn't exist, it will get created.
:::

## Reading
To access to the content of the prefs file you can use the [`content`](./api/prefs/#content) property, but that is useless since the `Prefs` class acts like a dictionary.
So, to access a key you can do it so
```py
my_prefs["lang"]
```
And if you try and print it, you will get:
```py
print(my_prefs)
>>> {'lang': 'en','theme': 'dark', 'scheme': {'background': '#AB2E6A', 'font-color': '#129396', 'font': 'UbuntuMono'}}
```

It is exactly the same as printing the `content` attribute:
```py
print(my_prefs.content)
>>> {'lang': 'en','theme': 'dark', 'scheme': {'background': '#AB2E6A', 'font-color': '#129396', 'font': 'UbuntuMono'}}
```

At this point you should be wondering «_How to access to the "background" value?_», well, it is quite easy:
```py
my_prefs["scheme/background"] # It is called key path
```

## Writing
To change the value of a key may want to use the [`write()`](./api/prefs/#write) method, but again, `Prefs` offers a dictionary-like interface, so:
```py
print(my_prefs["lang"])
>>> en

my_prefs["lang"] = "es"

print(my_prefs["lang"])
>>> es
```

And to change the value of `background`, use it's key path.
```py
print(my_prefs["scheme/background"])
>>> #AB2E6A

my_prefs["scheme/background"] = "#56B8D1"

print(my_prefs["scheme/background"])
>>> #56B8D1
```

Any key that doesn't exist in the key path, will get created.  
So we can do this:
```py
my_prefs["scheme/font/family"] = "UbuntuMono"
my_prefs["scheme/font/color"] = "#129396"
my_prefs["scheme/font/size"] = 15
```
:::info
Nested assigment doesn't work.
```py
my_prefs["scheme"]["font"]["family"] = "UbuntuMono" # Is not valid and won't work
```
You need to use key path, as the above example.
:::

The prefs file will look like:
```py
#PREFS
lang='en'
theme='dark'
scheme=>
    background='#56B8D1'
    font-color='#129396'
    font=>
        size=15
        family='UbuntuMono'
        color='#129396'
```
But there is problem, we don't need `font-color` anymore, we need to remove it, how?

## Removing
To remove keys from the prefs file you can use the `pop` method (like a dictionary).
```py
my_prefs.pop("scheme/font-color") # Key path is allowed
```
Which will end up in:
```py
#PREFS
lang='en'
theme='dark'
scheme=>
    background='#56B8D1'
    font=>
        size=15
        family='UbuntuMono'
        color='#129396'
```

## More
There are more useful methods, check them at the API reference:
- [`write_many()`](./api/prefs#write_many).
- [`overwrite()`](./api/prefs#overwrite).
- [`to_json()`](./api/prefs#to_json).
- [`to_yaml()`](./api/prefs#to_yaml).

And some useful functions that you can see at [Functions](./api/functions).

:::note
If you are building an application, check [PREFS resoureces](./resources).
:::
