def remove_comments(string: str, comment: str="#") -> str
	in_string = False # If iterating in string ignore comments otherwise don't 
	quote = "" # Type of quote (simple or double), because you can't open a string with simple quotes and close it with double

	for e, char in enumerate(string): # Iterate thorught the string
		if char == "'" or char == '"': # Checks if the current character is a quote
			if e != 0: # Checks if the quote isn't in the first place
				if string[e -1] == "\\": # Checks if the character before it is a backslahs
					continue # If it is ignore it

			if quote == char or not in_string: # If the type of quote is the current char, or if isn't in a string
				quote = char # Set the quote to the char
				in_string =  not in_string # And set in_string to True if False and viceversa

		if char == comment and not in_string: # If the current character is the comment character and isn't in a string
			string = string[:e] # Cut string until here
			break # And break

	return string # Return the string

with open("trial.prefs") as file:
	lines = [line.rstrip('\n') for line in file]
	lines = list(map(lambda x: remove_comments(x), lines))

	[print(i) for i in lines]

