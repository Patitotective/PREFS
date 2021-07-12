import __init__ as PREFS
import inspect
import mdutils

def GetDocs():
	prefsDocs = inspect.getmembers(PREFS) # Module PREFS
	prefsPrefsDocs = inspect.getmembers(PREFS.PREFS) # Class PREFS inside PREFS module
	prefsPrefsParam = GetParameters(PREFS.PREFS)

	# print( [type(i) for i in prefsDocs] )
	# print( [type(i) for i in prefsPrefsDocs] )
	# print( type(i) for i in prefsPrefsParam ) 

	# prefsDocs = [i[0] for i in inspect.getmembers(PREFS)] # Module PREFS
	# prefsPrefsDocs = [i[0] for i in inspect.getmembers(PREFS.PREFS)] # Class PREFS inside PREFS module

	for i in [prefsDocs, prefsPrefsDocs, prefsPrefsParam]:
		i = filter(FilterBuiltInFunctionAnLibraries, i)
		i = list(i)

	# print(docs)

	result = {"PREFS": {}, "PREFS.PREFS": {}, "PREFS.PREFSParam": {}}
	
	for i in prefsDocs:
		# pass
		result["PREFS"][i[0]] = inspect.getdoc(i[1]).replace("\n", "\t")

	for i in prefsPrefsDocs:
		# pass
		result["PREFS.PREFS"][i[0]] = inspect.getdoc(i[1]).replace("\n", "\t")

	for i in prefsPrefsParam:
		# pass
		result["PREFS.PREFSParam"][i[0]] = i

	return result

def FilterBuiltInFunctionAnLibraries(x):
	if x[0].startswith("__") and x[0].endswith("__") or x[0] in ["json", "ast", "os", "path", "pypistats", "warnings"]:
		return False

	return True

def GetParameters(obj: any):
	signature = inspect.signature(obj)

	return [str( signature.parameters[i] ) for i in signature.parameters]

def CreateDocsMDFile():
	mdFile = mdutils.MdUtils(file_name='Advanced',title='Advanced')

	mdFile.new_header(level=2, title="PREFS class parameters")


	mdFile.create_md_file()



prefs = lambda: GetDocs()
DocsPrefs = PREFS.PREFS(prefs, filename="docs", filterPrefs=(lambda x: x.replace("\n", "\t"), lambda x: x.replace("\t", "\n")))

# print(DocsPrefs.file["PREFS"])
# print( inspect.signature(PREFS.PREFS) )
#print(PREFS.PREFS.__dict__.keys())
# print(GetDocs())
