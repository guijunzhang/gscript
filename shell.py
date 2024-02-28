import gscript

print("Enter 'exit' to exit terminal")

while True:
	text = input('gscript > ')

	if (text == 'exit'): 
		print('Done!')
		break

	result, error = gscript.run('stdin', text)

	if error: print(error.as_string())
	else: print(result)