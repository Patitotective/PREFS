# Tests
To run the tests do
```sh
pytest tests
```
(Remember to do it inside your virtual enviroment with `prefs` installed)

## Test bundle
```sh
prefs bundle prefs.prefs
```
They have to print out the same
```sh
prefs read prefs.prefs
prefs read prefs_resource.py
```
