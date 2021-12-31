"""
Run the tests with:
```
python -m unittest
```
Where python is your python interpreter.
(Remember to do it inside the tests directory)
"""
import os
import unittest
import prefs


class TestPrefs(unittest.TestCase):
    PATH = "prefs.prefs"
    DEFAULT_PREFS = {
        "theme": "light", 
        "scheme": {
            "background": "#ffffff", 
            "font": "UbuntuMono", 
        }, 
        "range1": range(100), 
        "range2": range(14, 84), 
        "range3": range(0, 30, 2), 
        "keybindings": {
            "duplicate": {
                "keys": "Ctrl+D", 
                "command": "dup", 
            }, 
            "cut": {
                "keys": "Ctrl+X", 
                "command": "cut", 
            }, 
            "enabled": False,
            "quit": {
                "keys": "Ctrl+Q", 
                "command": "qut", 
            }, 
            "secret": b"aliens do exist, outside earth"
        }, 
        "lang": "en", 
    }

    def setUp(self):
        self.maxDiff = None
        self.my_prefs = prefs.Prefs(self.DEFAULT_PREFS, self.PATH)
        self.my_prefs.overwrite()

    def tearDown(self):
        self.assertEqual(self.my_prefs.content, self.DEFAULT_PREFS)

    def test_version(self):
        self.assertEqual(prefs.__version__, "0.3.0")
    
    def test_write(self):        
        self.DEFAULT_PREFS["lang"] = "es"
        self.my_prefs["lang"] = "es"

    def test_pop(self):
        self.DEFAULT_PREFS.pop("lang")
        self.my_prefs.pop("lang")

    def write_nested(self):
        self.DEFAULT_PREFS["keybindings"]["copy"]["keys"] = "Ctrl+Shift+C"
        self.my_prefs.write("keybindings/copy/keys", "Ctrl+Shift+C")

    def test_write_many(self):
        self.DEFAULT_PREFS["theme"] = "dark"
        self.DEFAULT_PREFS["lang"] = "en"

        self.my_prefs.write_many(
            {
                "theme": "dark", 
                "lang": "en"
            }, 
        )

'''
class ZxyPrefsEnd(unittest.TestCase):
    """It is called this way to be executed at the end of TestPrefs.
    """
    def test_end(self):
        if os.path.isfile(TestPrefs.PATH):
            os.remove(TestPrefs.PATH)
'''

class TestPrefsSyntax(unittest.TestCase):
    """Test PREFS syntax errors.
    """
    def test_key_val(self):
        """Test emtpy key or val.
        """
        with self.assertRaises(SyntaxError):
            string = """
            a=
            =1
            """

            my_prefs = prefs.parse(string)

    def test_sep(self):
        """Test no separator.
        """
        with self.assertRaises(SyntaxError):
            string = """
            a
            1
            """

            my_prefs = prefs.parse(string)

    def test_indent(self):
        """Test indentation edge cases.
        """
        with self.assertRaises(SyntaxError):
            string = """
            a=>
            lol=True
            """

            my_prefs = prefs.parse(string)

    def test_types(self):
        with self.assertRaises(TypeError):
            my_prefs = prefs.to_prefs(
                {
                    "func": lambda x: x+1, 
                    "list": [1, "a", ["b", self]], 
                    "set": {1, 2, 3, 2, "a", self.test_sep}, 
                    "dict": {
                        "1": TestPrefs, 
                        "2": os
                    }
                }
            )
