import subprocess
import PREFS
import ast
import theme_resource

def test1():
	"""Test read_prefs_file command in CLI tool.
	"""
	result = subprocess.check_output(["PREFS", "read_prefs_file", "prefs1.prefs"]).strip().decode("utf-8")

	assert ast.literal_eval(result) == PREFS.read_prefs_file("prefs1.prefs")

def test2():
	"""Test convert_to_prefs command in CLI tool:
	"""
	prefs = str(PREFS.read_prefs_file('prefs2.prefs'))
	result = subprocess.check_output(["PREFS", "convert_to_prefs", prefs]).strip().decode("utf-8")

	with open("prefs2.prefs", "r") as file:
		assert file.read().strip() == result

def test3():
	"""Test bundle command in CLI tool
	"""
	subprocess.run(["PREFS", "bundle", "theme.prefs"])

	assert PREFS.read_prefs_file("theme.prefs") == PREFS.read_prefs_file(":/theme.prefs")

if __name__ == "__main__":
	test1()
	test2()
	test3()

	print("Everything OK")
