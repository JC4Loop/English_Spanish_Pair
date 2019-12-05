def ContainsNonEngChars(string):
	rBool = False
	if 'Ã¡' in string:
		#á
		rBool = True
	if 'Ã‰' in string:
		#É
		rBool = True
	if 'Ã³' in string:
		#é
		rBool = True
	if 'Ãº' in string:
		#ú
		rBool = True
	return rBool

def replaceWithLatin1Char(string):
	if 'Ã¡' in string:
		#á
		string = string.replace('Ã¡', '\xe1')
	if 'Ã‰' in string:
		#É
		string = string.replace('Ã‰', '\xc8')
	if 'Ã³' in string:
		#é
		string = string.replace('Ã³', '\xe9')
	if 'Ãº' in string:
		#ú
		string = string.replace('Ãº', '\xfa')
	return string
