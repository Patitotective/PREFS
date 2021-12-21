# Libraries
import os
import prefs
import unittest


class TestPrefs(unittest.TestCase):
    PATH = "prefs.prefs"
    DEFAULT_PREFS = {
        "theme": "light", 
        "lang": "en", 
        "keybindings": {
            "duplicate": {
                "keys": "Ctrl+D", 
                "command": "dup", 
            }, 
            "copy": {
                "keys": "Ctrl+C", 
                "command": "cop", 
            }, 
            "paste": {
                "keys": "Ctrl+V", 
                "command": "pas", 
            }, 
            "cut": {
                "keys": "Ctrl+X", 
                "command": "cut", 
            }, 
            "quit": {
                "keys": "Ctrl+Q", 
                "command": "qut", 
            }
        }
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

            my_prefs = prefs.from_string(string)

    def test_sep(self):
        """Test no separator.
        """
        with self.assertRaises(SyntaxError):
            string = """
            a
            1
            """

            my_prefs = prefs.from_string(string)

    def test_indent(self):
        """Test indentation edge cases.
        """
        with self.assertRaises(SyntaxError):
            string = """
            a=>
            lol=True
            """

            my_prefs = prefs.from_string(string)

if __name__ == "__main__":
    val = [[lambda x: x ** 2]]
    my_prefs = prefs.Prefs({"list": val})
    print(my_prefs["list"])
