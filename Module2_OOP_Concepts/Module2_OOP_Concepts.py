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

#class Employee:
#	def __init__(self,fname,ip):
#		self.name = fname
#		self.addr = ip
#	def display(self):
#		print(self.name)

#e1=Employee('Hi', 32)
#e2=Employee('Hello',56)

#print(e2.__dict__)


"""
* Constructor in Python

- Special method used for initializing objects with attributes
- It is __init__() method
- First arguments is 'self.

* TYpes of constructor:

- Parameterized constructor
- Non-Parameterized constructor
- Default constructor
"""

#class Employee:
#	def __init__(self):
#		self.fname = 'Pat'
#		self.ip = 32

#e1 = Employee()
#e2 = Employee()
#print(e1.__dict__)

#without constructor: object cannot be created

"""
* How OOP Works

1. memory allocation for object
2. memory reference returned to the object
3. memory reference automatically passed inside constructor
4. constructor creates/initialize variables at that memory reference
"""


"""
* Accessing Class Members Outside the Class
"""

#class Employee:
#	def __init__(self,ip,name):
#		self.addr = ip
#		self.fname = name

#	def display(self):
#		print(f"ip is {self.addr} and fname is {self.fname}")

#e1 = Employee(24, 'Hi')
#e2 = Employee(12, 'Pat')

#print(e2.__dict__)
#accessing attribute outside the class
#print(e2.addr)
#e2.addr = 10000 #updating attribute
#print(e2.addr)

#e2.display()


"""
* Built in Class Functions

- getattr(object_name, attribute_name)
- setattr(object_name, attribute_name, new_value)
- delattr(object_name, attribute_name)
- hasattr(object_name, attribute_name)
"""

#class Employee:
#	def __init__(self,name,ip):
#		self.fname = name
#		self.addr = ip

#e1 = Employee('Hi', 568)
#e2 = Employee('Hi', 1250)
#print(getattr(e2, 'addr')) #1250
#setattr(e2, 'addr', 56000)
#print(e2.__dict__)
#delattr(e2, 'addr')
#print(e2.__dict__)

#print(hasattr(e1, 'fname'))


"""
* Built in Class Attributes

- __dict__:- Dictionary containing class's namespace
- __doc__:- Class documentation
- __name__:- Class Name
- __module__:- Module name in which class is defined
- __bases__:- List of base classes
"""

#class Employee:
	"""This is employee class for maintaining employee data"""
#	def __init__(self,ip,name):
#		self.addr = ip
#		self.fname = name
#	def display(self):
#		print(f"addr is {self.addr} and fname is {self.fname}")

#e1 = Employee(760000, 'Hi')
#e2 = Employee(707650, 'Hello')

#print(Employee.__doc__)
#print(Employee.__dict__)
#print(Employee.__name__)
#print(Employee.__module__)

"""
* isInstance() Function in Python
"""