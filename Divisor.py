Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def divisor():
	num = int(input('Choose a number: '))
	for i in range(num):
		if num % (i + 1) == 0:
			print(i + 1)

			
>>> divisor()
Choose a number: 176
1
2
4
8
11
16
22
44
88
176
>>> 
