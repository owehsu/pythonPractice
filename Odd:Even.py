Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def oddEven():
	number = int(input('Choose a number: '))
	if number % 2 == 0 {
		
SyntaxError: invalid syntax
>>> def oddEven():
	number = int(input('Choose a number: '))
	if number % 2 == 0:
		print('Even number!')
	elif number % 2 == 1:
		print('Odd number!')
	else:
		print('Invalid!')
