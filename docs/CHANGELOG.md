# Change Log

#### v0.1.9 (07/08/2021)
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


#### v0.1.8 (31/07/2021)

- Fixed bug when creating a pref with an empty dictionary as value.
---

#### v0.1.7 (20/07/2021)

- Added `ConvertToPREFS()` function (outside PRFS class) that do the same as `dumps()` in json. Converts a dictionary into a PREFS file but instead of writing the PREFS in a file returns it as string.
- Changed `ReadPrefs()` function name (outside PREFS class) to `ReadPREFSFile()`.
- Fixed issue when dictionary=True parameter, fixed issue when dictionary=True and interpret=True parameter.

---

#### 0.1.6 (18/07/2021)

Added ReadPrefs function outside PREFS class that reads a PREFS file and return it's value.

---

#### 0.1.4 (16/07/2021)

Fixed error when overwriting prefs and using a lambda function.

---

#### 0.1.3 (11/07/2021)

Added tree/cascade (nested dictionaries) support.

---

Added docstring.

---

#### 0.0.86 (17/06/2021)

Fixed path support, fixed ChangeFilename function, added debug parameter.

---

#### 0.0.85 (16/06/2021)

Fixed little issues.

---

#### 0.0.81 (05/06/2021)

Added dictionary write mode and support path file.

---

#### 0.0.80 (05/06/2021)

Added ChangeFilename() function and ReWritePrefs() function.

---

#### 0.0.65 (04/05/2021)

Set max split as 1.

---

#### 0.0.6 (04/05/2021)

Now you can choose your PREFS ender, line break is predetermined, remember don't put a character that is on your PREFS because program fails.

---

#### 0.0.46 (04/05/2021)

Fixed error with lambda.

---

#### 0.0.45 (02/05/2021)

Now in class PREFS argument PREFS you must pass a lambda: function for not execute the function always, only when file is lost.

---

#### 0.0.4 (02/05/2021)

Added python interpreter for pref values (using ast library)

---

#### 0.0.3 (02/05/2021)

Name change

---

#### 0.0.2 (01/05/2021)

---

#### 0.0.1 (01/05/2021)

First Release
