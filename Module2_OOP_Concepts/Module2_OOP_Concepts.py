"""
Object-Oriented Programming(OOP) is an approach of writing programs by
creating classes and objects.

Why OOP ?

To solve real-world problems effectively.
"""

"""
1 - Creating Class and Object

Class: is a user-defined datatype.
"""

#def demo():
#	print("Hello")
#print(type(demo))

"""
class Class_name:
	#attributes
	#attributes

obj1 = Class_name([args])
obj2 = Class_name([args])
"""

#class Email:
#	pass

#e1=Email()
#e2=Email()

#print(type(e1))

class Employee:
	def __init__(self,fname,ip):
		self.name = fname
		self.addr = ip
	def display(self):
		print(self.name)

e1=Employee('Hi', 32)
e2=Employee('Hello',56)

print(e2.__dict__)