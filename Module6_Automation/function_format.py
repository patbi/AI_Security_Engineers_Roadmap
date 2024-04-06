x = 'Hello'
y = 50
z = 73.9

#print('Student\'s name is {2} and his age is {0} and his grade is {1}'.format(x,y,z))
print('Student\'s name is {:10} and his age is {:10} and his grade is {:10}'.format(x,y,z))


for i in range(1,11):
	print("{:5}{:5}{:5}".format(i,i*i,i*i*i))
	