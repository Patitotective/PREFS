# Changelog
### v1.0.1 (03/01/2022)
- Fixed bug when trying to read a PREFS file using the `read` function.
- Removed JSON and YAML suppport
	- `PrefsBase.to_json`
	- `PrefsBase.to_yaml`
	- `read_json`
	- `read_yaml`

### v1.0.0 (03/01/2022)
- New parse system using [_Lark_](https://github.com/lark-parser/lark).
	- Using _Lark_ indenting with spaces or tabs is allowed.
- Added support for bytes and ranges types.
- Now it checks what objects are written into the prefs file to avoid errors.
- Improved CLI tool with [_Click_](https://click.palletsprojects.com).
- Better tests with _unittest_.
- Now using poetry.
- Improved code quality in general.
- Ordered directories layout.
- Added dictionary-like interface for the `Prefs` class:
	- `Prefs.__str__`
	- `Prefs.__repr__`
	- `Prefs.__len__`
	- `Prefs.__delitem__`
	- `Prefs.__getitem__`
	- `Prefs.__setitem__`
	- `Prefs.__contains__`
	- `Prefs.__iter__`
	- `Prefs.keys`
	- `Prefs.values`
	- `Prefs.items`
	- `Prefs.pop`
	- `Prefs.get`
	- `Prefs.has_key`
	- `Prefs.clear`
	- `Prefs.update`
	- `Prefs.popitem`
- Renamed:
	- `PrefsBase.file` -> `PrefsBase.content`
	- `PrefsBase.read_prefs` -> `PrefsBase.read`
	- `PrefsBase.write_prefs` -> `PrefsBase.write`
	- `PrefsBase.write_multiple_prefs` -> `PrefsBase.write_many`
	- `PrefsBase.overwrite_prefs` -> `PrefsBase.overwrite`
	- `PrefsBase.delete_file` -> `PrefsBase.delete`
	- `PrefsBase.convert_to_json` -> `PrefsBase.to_json`
	- `PrefsBase.convert_to_yaml` -> `PrefsBase.to_yaml`
	- `convert_to_prefs` -> `to_prefs`
	- `read_prefs_file` -> `read`
	- `read_json_file` -> `read_json`
	- `read_yaml_file` -> `read_yaml`
- Renamed CLI commands:
	- `read_prefs_file` -> `read`
- New:
	- `PrefsBase.get`
	- `PrefsBase.remove_key`
	- `bundle`
	- `parse`
- New CLI commands:
	- `about`
- Removed:
	- `Prefs.change_filename`
- Removed CLI commands:
	`convert_to_prefs`

### v0.2.65 (22/10/2021)
- Improved error messages.
- Improved efficiency.
- Removed `indent_char` parameter from `PrefsBase` class.
- Now you MUST to indent with tabulations `\t`.

### v0.2.60 (20/10/2021)
- When adding a prefs file as a data when using _pyinstaller_ now it can read the file.
- Added `output` parameter in `convert_to_prefs` function.

### v0.2.56 (16/10/2021)
- Added resources suport so you can build your app without any issue.
- Added CLI tool.
- Cleaned directory tree.
- Fixed small bugs.
- Renamed `PREFSBase` to `PrefsBase`.
- Renamed `PREFS` to `Prefs`.
- Removed `separator_char, ender_char, continuer_char, comment_char, interpret, cascade` parameters from `PrefsBase` class.
- Updated tests.
- Updated discord username.
- Updated `EXTRAINFO.md`.

### v0.2.51 (24/09/2021)
- Fixed bug filename has no path (`prefs.prefs`).

### v0.2.50 (16/09/2021)
- `PREFSBase` class
	- Now `filename` parameter includes the extension too.
	- Fixed path detection on `create_prefs`
	- Now writes the representation of a string, not just the string with quotes around it.
	- Now it uses `ast.literal_eval` insead of `eval` to evaluate strings.
	- Now `separator_char`, `ender_char`, `continuer_char` and `comment_char` are constantes (no parameters).
	- Now `file` attribute it's an property method that calls `read_prefs`.
	- Removed `dictionary` parameter.
	- Setted split to 1 when splitting key and value.
	- Added `dump` method that returns an string with `prefs` dictionary as PREFS format.

- Added `VERSION` constant variable.
- Added `split_path` function.
- Added `accumulate_list` function.

### v0.2 (17/08/2021)
- Added `write_multiple_prefs` function which requires a list of prefs and a list of values to change. With this function writing multiple prefs will be more efficiently. 

### v0.1.99 (16/08/2021)
- Added `auto_generate_keys` parameter. 

### v0.1.98 (08/08/2021)
- Added `indent` parameter. 
- Comment your own PREFS files (and change the comment character `#`).

### v0.1.95 (08/08/2021)
- Deleted `readPREFS.py` and `createPREFS.py`.
- Added `PREFS_Base` class and changed `read_prefs_file` function and `convert_to_prefs` function using `PREFS_Base` class.

### v0.1.91 (07/08/2021)
- Replaced:
	```py 
	import sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

	from readPREFS import ReadPREFS
	from createPREFS import CreatePREFS
	```
	With:
	```py
	if __name__ == '__main__':
		from readPREFS import ReadPREFS
		from createPREFS import CreatePREFS
	else:
		from .readPREFS import ReadPREFS
		from .createPREFS import CreatePREFS
	```

### v0.1.9 (07/08/2021)
- Changed all function names accord to PEP8:
	* `PREFS.ReadPrefs` -> `PREFS.read_prefs`
	* `PREFS.WritePrefs` -> `PREFS.write_prefs`
	* `PREFS.OverWritePrefs` -> `PREFS.overwrite_prefs`
	* `PREFS.ChangeFilename` -> `PREFS.change_filename`
	* `PREFS.ConvertToJson` -> `PREFS.convert_to_json`
	* `ReadJsonFile` -> `read_json_file`
	* `ReadPREFSFile` -> `read_prefs_file`
	* `ConvertToPREFS` -> `convert_to_prefs`

- Added `PREFS.convert_to_yaml` and `read_yaml_file`.

### v0.1.8 (31/07/2021)
- Fixed bug when creating a pref with an empty dictionary as value.

### v0.1.7 (20/07/2021)
- Added `ConvertToPREFS()` function (outside PRFS class) that do the same as `dumps()` in json. Converts a dictionary into a PREFS file but instead of writing the PREFS in a file returns it as string.
- Changed `ReadPrefs()` function name (outside PREFS class) to `ReadPREFSFile()`.
- Fixed issue when dictionary=True parameter, fixed issue when dictionary=True and interpret=True parameter.

### 0.1.6 (18/07/2021)
- Added ReadPrefs function outside PREFS class that reads a PREFS file and return it's value.

### 0.1.4 (16/07/2021)
- Fixed error when overwriting prefs and using a lambda function.

### 0.1.3 (11/07/2021)
- Added tree/cascade (nested dictionaries) support.
- Added docstring.

### 0.0.86 (17/06/2021)
- Fixed path support, fixed ChangeFilename function, added debug parameter.

### 0.0.85 (16/06/2021)
- Fixed little issues.

### 0.0.81 (05/06/2021)
- Added dictionary write mode and support path file.

### 0.0.80 (05/06/2021)
- Added ChangeFilename() function and ReWritePrefs() function.

### 0.0.65 (04/05/2021)
- Set max split as 1.

### 0.0.6 (04/05/2021)
- Now you can choose your PREFS ender, line break is predetermined, remember don't put a character that is on your PREFS because program fails.

### 0.0.46 (04/05/2021)
- Fixed error with lambda.

### 0.0.45 (02/05/2021)
- Now in class PREFS argument PREFS you must pass a lambda: function for not execute the function always, only when file is lost.

### 0.0.4 (02/05/2021)
- Added python interpreter for pref values (using ast library)

### 0.0.3 (02/05/2021)
- Name change

### 0.0.2 (01/05/2021)
- ...

### 0.0.1 (01/05/2021)
- First Release
