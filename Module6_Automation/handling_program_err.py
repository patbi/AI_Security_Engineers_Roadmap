a = int(input('Please, insert first number: \t'))
b = int(input('Please, insert second number: \t'))

try:
	c = a / b
except:
	print('You cannot divide',a, 'by',b)
else:
	print(c)