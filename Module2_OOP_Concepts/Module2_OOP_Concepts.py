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
#	"""This is employee class for maintaining employee data"""
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


#class Isinstance:
#	pass
#s1 = Isinstance()
#class Employee:
#	"""This is employee class for maintaining employee data"""
#	def __init__(self,ip,name):
#		self.addr = ip
#		self.fname = name
#	def display(self):
#		print(f"addr is {self.addr} and fname is {self.fname}")

#e1 = Employee(760000, 'Hi')
#e2 = Employee(707650, 'Hello')

#print(isinstance(s1,Employee))


"""
* Instance variables & instance methods

1 - Types of variables:
	- Instance Variables
		* Variables made for particular instance
		* Separate copy is created for every object
		* Values of variables differs from object to object
		* Modication in one object won't effect other objects
	
2 - Class Variables

	Creating instance variables
		- Using constructor
		- Using instance method
		- Outside class
"""

#class Employee:
#	def __init__(self, ip, name):
#		self.addr = ip
#		self.fname = name

#	def display(self):
#		print(self.addr,self.fname)

#	def change_data(self):
		#self.addr = 850000
#		self.addr = int(input("enter new addr:"))
		#self.fname = 'Pat'
#		self.fname = input("enter new fname")


#emply1 = Employee(9000, 'Hi')
#emply2 = Employee(56000, 'Hello')
#- outside the class
#- emply2.company= 'Thenavigo'
#- print(emply2.__dict__)
#- emply1.display()

#emply2.change_data()
#print(emply2.__dict__)

"""
* Class variables:

- Variables made for entire class (All objects)
- Only one copy is created and distributed to all objects
- Modification in class variable impact on all objects

& Class methods:

- Method which works on class variables
- First argument is class reference
- Made using decorator '@classmethod'
"""

#class Employee:
#	company_name = "Thenavigo" #class variable
#	def __init__(self,ip,name):
#		self.addr = ip
#		self.fname = name

#	@classmethod
#	def get_company_name(cls):
		#cls.company_name = 'new_name'
		#print(cls.company_name)
#		print(f"company name is:", cls.company_name)

#e1 = Employee(657, 'Hello')
#e2 = Employee(35000, 'Hi')

#print(Employee.company_name) #Thenavigo
#print(e1.company_name) #Thenavigo

#print(e2.__dict__)
#e2.company_name = "example"
#print(e2.__dict__)
#Employee.get_company_name()


"""
* Stter and Getter Methods

Instance methods:

- setter method:- set values of instance variables
- getter method:- get values of instance variables
"""

#class Employee:
#	def setName(self,name):  #setter
#		self.fname = name

#	def getName(self):       #getter
#		print("The fname is", self.fname)

#e1 = Employee()
#e2 = Employee()

#e1.setName(input("Enter the fname:"))
#e2.setName(input("Enter the fname:"))
#print("e1 object is:",e1.__dict__)
#print("e2 object is:",e2.__dict__)
#e1.getName()
#e2.getName()


"""
* Staticmethod in Python
"""

