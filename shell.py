import gscript

while True:
	text = input('gscript > ')
	result, error = gscript.run('stdin', text)

	if error: print(error.as_string())
	else: print(result)