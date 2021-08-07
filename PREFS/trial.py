import sys, os
import __init__ as PREFS

# '''
prefs ={
	"week1": {
		"monday": {
			"math": "8:00", 
			"language": "9:00"
			}, 
		"tuesday": {
			"draw": "10:00", 
			"spanish": "11:00"
			},
		},  
	"week2": {
		"wednesday": {
			"art": "12:00", 
			"logic": "13:00"
			}, 
		"thursday": {
			"phisics": "14:00", 
			"english": "15:00"
			}
		}
	}
# '''

# prefs = {"lang": "en", "keybindings": {"Ctrl+C": "Copy", "Ctrl+V": "Paste", "Ctrl+X": "Cut"}}

user_prefs = PREFS.PREFS(prefs, filename="trial")
user_prefs.overwrite_prefs()
print(user_prefs.file)
#file = PREFS.read_yaml_file("trial")
#print(file)
# prefs = PREFS.PREFS(PREFS.ReadPREFSFile("idea"))
