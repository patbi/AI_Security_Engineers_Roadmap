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

# def demo():
#	print("Hello")
# print(type(demo))

"""
class Class_name:
	#attributes
	#attributes

obj1 = Class_name([args])
obj2 = Class_name([args])
"""

# class Email:
#	pass

# e1=Email()
# e2=Email()

# print(type(e1))

# class Employee:
#	def __init__(self,fname,ip):
#		self.name = fname
#		self.addr = ip
#	def display(self):
#		print(self.name)

# e1=Employee('Hi', 32)
# e2=Employee('Hello',56)

# print(e2.__dict__)


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

# class Employee:
#	def __init__(self):
#		self.fname = 'Pat'
#		self.ip = 32

# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)

# without constructor: object cannot be created

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

# class Employee:
#	def __init__(self,ip,name):
#		self.addr = ip
#		self.fname = name

#	def display(self):
#		print(f"ip is {self.addr} and fname is {self.fname}")

# e1 = Employee(24, 'Hi')
# e2 = Employee(12, 'Pat')

# print(e2.__dict__)
# accessing attribute outside the class
# print(e2.addr)
# e2.addr = 10000 #updating attribute
# print(e2.addr)

# e2.display()


"""
* Built in Class Functions

- getattr(object_name, attribute_name)
- setattr(object_name, attribute_name, new_value)
- delattr(object_name, attribute_name)
- hasattr(object_name, attribute_name)
"""

# class Employee:
#	def __init__(self,name,ip):
#		self.fname = name
#		self.addr = ip

# e1 = Employee('Hi', 568)
# e2 = Employee('Hi', 1250)
# print(getattr(e2, 'addr')) #1250
# setattr(e2, 'addr', 56000)
# print(e2.__dict__)
# delattr(e2, 'addr')
# print(e2.__dict__)

# print(hasattr(e1, 'fname'))


"""
* Built in Class Attributes

- __dict__:- Dictionary containing class's namespace
- __doc__:- Class documentation
- __name__:- Class Name
- __module__:- Module name in which class is defined
- __bases__:- List of base classes
"""

# class Employee:
#	"""This is employee class for maintaining employee data"""
#	def __init__(self,ip,name):
#		self.addr = ip
#		self.fname = name
#	def display(self):
#		print(f"addr is {self.addr} and fname is {self.fname}")

# e1 = Employee(760000, 'Hi')
# e2 = Employee(707650, 'Hello')

# print(Employee.__doc__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)

"""
* isInstance() Function in Python
"""

# class Isinstance:
#	pass
# s1 = Isinstance()
# class Employee:
#	"""This is employee class for maintaining employee data"""
#	def __init__(self,ip,name):
#		self.addr = ip
#		self.fname = name
#	def display(self):
#		print(f"addr is {self.addr} and fname is {self.fname}")

# e1 = Employee(760000, 'Hi')
# e2 = Employee(707650, 'Hello')

# print(isinstance(s1,Employee))


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

# class Employee:
#	def __init__(self, ip, name):
#		self.addr = ip
#		self.fname = name

#	def display(self):
#		print(self.addr,self.fname)

#	def change_data(self):
# self.addr = 850000
#		self.addr = int(input("enter new addr:"))
# self.fname = 'Pat'
#		self.fname = input("enter new fname")


# emply1 = Employee(9000, 'Hi')
# emply2 = Employee(56000, 'Hello')
# - outside the class
# - emply2.company= 'Thenavigo'
# - print(emply2.__dict__)
# - emply1.display()

# emply2.change_data()
# print(emply2.__dict__)

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

# class Employee:
#	company_name = "Thenavigo" #class variable
#	def __init__(self,ip,name):
#		self.addr = ip
#		self.fname = name

#	@classmethod
#	def get_company_name(cls):
# cls.company_name = 'new_name'
# print(cls.company_name)
#		print(f"company name is:", cls.company_name)

# e1 = Employee(657, 'Hello')
# e2 = Employee(35000, 'Hi')

# print(Employee.company_name) #Thenavigo
# print(e1.company_name) #Thenavigo

# print(e2.__dict__)
# e2.company_name = "example"
# print(e2.__dict__)
# Employee.get_company_name()


"""
* Setter and Getter Methods

Instance methods:

- setter method:- set values of instance variables
- getter method:- get values of instance variables
"""

# class Employee:
#	def setName(self,name):  #setter
#		self.fname = name

#	def getName(self):       #getter
#		print("The fname is", self.fname)

# e1 = Employee()
# e2 = Employee()

# e1.setName(input("Enter the fname:"))
# e2.setName(input("Enter the fname:"))
# print("e1 object is:",e1.__dict__)
# print("e2 object is:",e2.__dict__)
# e1.getName()
# e2.getName()


"""
* Staticmethod in Python:

- Methods which performs operations on external data
- It can also perform operations on class data
- No need to pass object or class reference
- Create using decorator '@staticmethod'

#    - Types of methods:    
#        * Instance methods
#        * Class methods
#        * Static methods
"""

# class Bank:
#    bank_name ='Hi'
#    rate_of_interest = 12.25
#    @staticmethod
#    def simple_interest(amount,n):
#        result = (amount*n*Bank.rate_of_interest)/100
#        print(result)

# amount = float(input("Enter principle amount"))
# n = int(input("Enter number of years:"))
# Bank.simple_interest(amount,n)

"""
4 - Inheritance in Python

* Inheritance deriving a new class from an existing class
so that new class inherits all members(attributes + methods)
of existing class is called as inheritance


#Old class: - Parent class, Base class,
#            Existing class, Super class

New class, sub class, derived class

* Object class:-
#    All classes in python are derived from built in 'object' class

* Creating child class:-

#    class Parent(object):
#        #attributes+methods

#    class Child(Parent):
#        #attributes+methods
"""

# class Employee:
#    bonus = 2000
#    def display(self):
#        print("This is employee class method")


# class Manager(Employee):
#    bonus1 = 10000
#    def show(self):
#        print("This is manager class method")

# e1 = Employee()
# m1 = Manager()

# e1.display()
# m1.show()
# print(m1.bonus)

"""
* Why we use inheritance ?

- For Code-reusability (write once use many times)
- When you have relations among classes

"""

# (No Inheritance used):

# class Customers:
#    - SetPersonalDetails()
#    - GetPersonalDetails()
#    - SetEducationDetails()
#    - GetEducationDetails()
#    - SetBankAccount()

# class Employee:
#    - SetPersonalDetails()
#    - GetPersonalDetails()
#    - SetEducationDetails()
#    - GetEducationDetails()
#    - SetBankAccount()
#    - SetSalary()
#    - SetBonus()

# (Inheritance used):

# class Customers:
#    - SetPersonalDetails()
#    - GetPersonalDetails()
#    - SetEducationDetails()
#    - GetEducationDetails()
#    - SetBankAccount()


# class Employee(Customers):
#    - SetBankAccount()
#    - SetSalary()
#    - SetBonus()


"""
* Constructor in Inheritance

How constructor works in inheritance:

- By default, constructor of parent class available to child class
"""

# class Parent:
#    def __init__(self):
#        print("Parent constructor called")
#        self.vehicule= "Scooter"

# class Child(Parent):
# def __init__(self):
# pass
# print("Child constructor called")
# self.vehicule = "BMW"


# c = Child()
# print(c.__dict__)

"""
* Super() function

- Using super() function, we can access parent class properties
- This function returns a temporary object which contains reference to parent class
- It makes inheritance more manageable and extensible
"""

# class Techcompany(object):
#    def __init__(self):
#        self.name = 'Thenavigo'
#        self.size = 100000
#        print("Techcompany class constructor called")

#    def display(self):
#        print("Hello world")


# class NonTechcompany(Techcompany):
#    def __init__(self):
#       super().display()
#       super().__init__()
#       self.type = 'LLC'
#       print("NonTechcompany class constructor called")

# Hi = NonTechcompany()
# print(Hi.__dict__)


"""
* Single and Multi-Level inheritance

#    - Types of Inheritance:
#       Depending on number of dhild and parent classes involved
#            - Single Inheritance
#                One Parent and one child class: Object --> Parent --> Child
#            - Multi-level Inheritance
#                Parent class and child class further inherited into new class forming multiple levels:
#                Object --> Parent --> Child --> Grand_Child
#            - Hierarchical Inheritance
#                One parent and multiple child classes: 
#                object--> Parent -->(child1, child2)
#            - Multiple Inheritance
#                Class is derived from multiple base classes.
#                Object --> (Parent1, Parent2) ==> Child
#            - Hybrid Ihneritance
                It contains multiple type of inheritance.
                Object-->(Parent1, Parent2) ==> (Child) ==> (Child1, Child2)
#            - Cyclic Inheritance

Let's see

- How constructor works
- How class variables and class methods work
- How Instance methods works
"""


# constructor in multi-level inheritance
# class Company(object):
#    def __init__(self):
#        print("Company constructor called")
#        self.name = input("Enter your name")

# class Employee(Company):
#    def __init__(self):
#        print("Company constructor called")
#        self.salary = float(input("Enter your salary:"))

# class Managers(Employee):
#    def __init__(self):
#        print("Managers constructor called")
#        self.bonus = float(input("Enter your bonus:"))

# m1 = Managers()

#- Hierarchical Inheritance

#class Company:
#    def __init__(self, name, ip):
#        self.fname = name
#        self.addr = ip
#    def display(self):
#        print("This is Company display method")

#class Employee(Company):
#    def __init__(self, name, ip, sal):
#        super(Employee, self).__init__(name, ip)
#        self.salary = sal
#    def display(self):
#        print("This is Employee display method")

#class Founder(Company):
#    def __init__(self, name, ip, s):
#        super(Founder, self).__init__(name, ip)
#        self.serial = s
#    def display(self):
#        print("This is Founder display method")

#f1 = Founder('Hi', 34, 100)
#print(f1.__dict__)

#e1 = Employee('Hello', 567, 4000000)
#print(e1.__dict__)

#c1 = Company('Thenavigo', 87000)
#print(c1.__dict__)


#- Multiple Inheritance syntax -

"""
#class Parent1(Object):
#    #parent1 class properties
class Parent2(Object):
#    #parent2 class properties
class Child(Parent1, Parent2):
#    #child class properties
"""

#class Country:
#    def __init__(self):
#        print("Country class constructor")
#        self.Office = 'Thenavigo'

#class State:
#    def __init__(self):
#        print("State class constructor")
#        self.Office = 'See-Docs'

#class District(State,Country):
#    def __init__(self):
#        super(District, self).__init__()
#        print("District class constructor")
#        self.Office = "DC"

#d = District()
#print(d.__dict__)


"""
- MRO:- Method Resolution Order
    MRO represents how properties (attributes+methods) are searched in inheritance.
    Rule-01:
        - Python First search in child class and then goes to parent class
        -  Priority is to child class
    
    Rule-02:
        - MRO Follows 'Depth First Left to Right approach'
    Rules-03:
    You can use mro(), method for knowing mro of any class objects
"""

#class A:
#    pass
#class B:
#    pass
#class C:
#    pass
#class X(A,B,C):
#    pass
#class Y(B,C):
#    pass
#class P(X,Y):
#    pass

#print(P.mro())


"""
5 - Encapsulation in Python

- Wrapping up data and methods working on data together in a single unit
(i.e class) is called as encapsulation

* Access Modifiers in Python:-

    - Generally, we restrict data access outside the class in encapsulation
    - Encapsulation can be achieved by declaring the data members and methods of a class as private
    - Three access specifiers:- public, private, protected
    
    - Public member:- Accessible anywhere by using oject reference
    - Private member:- Accessible within the class. Accessible via methods only
    - Protected member:- Accessible within class and it's subclasses


* Advantages :

  - Security
  - Prevents accidental modifications
  - Simplicity

"""

#class Finance:
#    def __init__(self):
#        self.__revenue = 20000  #private data
#        self._number_of_sales = 224   #protected data
#        #self.__number_of_sales = 224  # private data

#    def display(self):
#        #print(f"revenue is: {self.__revenue} and number of sales: {self.__number_of_sales}")
#        #self.__revenue = 40000
#        print(f"revenue is: {self.__revenue} and number of sales: {self.__number_of_sales}")

#f1 = Finance()
#-f1.display()
#-print(f1.__dict__)

#print(__revenue)
#print(revenue)

#print(f1.__dict__)

#class HR:
#    def __init__(self):
#        self.number_of_empl = 40000000
#        f1.__revenue = 5 # '_HR__revenue': 5 =>> _classname__variable

#h1 = HR()
#print(f1.__dict__)


"""
6 - Polymorphism in Python.

    - Polymorphism in python is an ability of python object
to take many forms.
    - If a variable, object, method performs different behaviour 
    according to situation is called as polymorphism.
"""

#example + :- python object
#print(10+20)  #30
#print("Hello"+"Hi")  #HelloHi

#len() function

#print(len("Hello"))   #5 #count number of characters
#print(len(['Hi','e','l','l','o']))  #5 #count number of items

#reversed() function
#tab = ["hi",'hello','welcome']
#company = "infosys"

#print("for tab now:")
#for i in reversed(company):
#    print(i)

#print("for list now:")
#for i in reversed(tab):
#    print(i)


"""
* Polymorphism with Inheritance
"""

#class Veh:
#    def __init__(self,name,ip,price):
#        self.fname = name
#        self.addr = ip
#        self.price = price

#    def get_details(self):
#        print("fname is:", self.fname)
#        print("addr is:", self.addr)
#        print("price is:", self.price)

#    def max_speed(self):
#        print("maximum speed limit is 100")

#    def gear(self):
#        print("gear change is 10")

#v1 = Veh("Truck", 675409, 50000000000000)
#v1.get_details()


#class Car(Veh):
#    def max_speed(self):
#        print("maximum speed limit is 340")

#    def gear(self):
#        print("gear change is 56")

#V1 = Veh("Truck", 54629, 50000000)
#C1 = Car("Car", 982340, 23000000)
#V1.get_details()
#C1.get_details()
#V1.max_speed()
#C1.max_speed()


"""
* Over-riding Built in Functions
"""

#class Cart:
#    def __str__(self):
#        return "This is cart class object"

#c1 = Cart()
#print(c1)

#class Cart:
#    def __init__(self,programming,data,mlai):
#        self.languages = programming
#        self.datamodeling = data
#        self.artificialintelligence = mlai

#    def __len__(self):
#        print("Total number of items in cart:")
#        return len(self.languages)+len(self.datamodeling)+len(self.artificialintelligence)

#Thenavigo = Cart(['Python1','Python2','Python3'],['tool1','tool2'],['ai'])
#print(len(Thenavigo))  #6


"""
* Polymorphism in Functions and Objects
"""

#class BMW:
#    def fuel_type(self):
#        print("Diesel")

#    def max_speed(self):
#        print("max speed is 500")

#class Ferrari:
#    def fuel_type(self):
#        print("Petrol")

#    def max_speed(self):
#        print("max speed is 780")

#def car_details(obj):
#    obj.fuel_type()
#    obj.max_speed()

#bmw = BMW()
#ferrari = Ferrari()

#car_details(bmw)
#print("---------")
#car_details(ferrari)


"""
* Operator Overloading in Python-01

    - When same operator behaves differently depending on values
    - You can assign a new meaning to operators also and you can extend
    functionality of operators.
    - You can change default behaviour of operator using over-riding.
"""
#num1 = 34
#num1 = "hello"
#num2 = 24
#num2 = "hi"
#print(num1+num2)  #58   #hellohi
#print(num1.__add__(num2))  #58
#print(num1.__add__(num2))
#print(int.__add__(num1,num2))
#print(str.__add__(num1,num2))
#print(dir(int))
#print(dir(str))

#step-1:- check datatype of left operand.  #int
#step2:- go in that class
#step3:- call __add__() function


"""
* Operator Overloading in Python-02
"""

#class Book:
#    def __init__(self,title,pages):
#        self.title = title
#        self.pages = pages

#    def __add__(self, other):  #(b1,b2)
#        total = self.pages+other.pages
#        return total


#b1 = Book('book1', 534)
#b2 = Book('book2', 876)
#b3 = Book('book3', 376)

#print("total number of pages:", b1.pages+b2.pages)
#print("total number of pages:", b1+b2) #b1.__add__(b2)  --> Book.__add__(b1,b2)


"""
* Overloading Comparison Operators in Python
"""

class Person:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    # overload < operator
    def __lt__(self, other):
        return self.addr < other.addr

p1 = Person("Alice", 20)
p2 = Person("Bob", 30)

print(p1 < p2)  # prints True
print(p2 < p1)  # prints False

#Operator Overloading in Python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)   # Output: (3,5)




class O:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age>other.age

o1 = O('O1', 200000)
o2 = O('O2', 10000)
print(o1>o2)