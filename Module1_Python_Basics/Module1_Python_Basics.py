"""
1 - Variables in Python
"""

#a = 9
#b = 16
#print(a)
#print(12)
#print(b)
#print(a * b * 5)
#fname = 'Data Engineer -'
#lname = 'ML/AI'
#print(fname+' '+lname)
#print(a,b,fname,lname)

"""
2 - Strings and Variables in Python 
"""

#name = "Patbi"
#ip = 12
#print("His name is",name,"and His ip is",ip)

#x = "2"
#y = '7'
#print(x + y)
#print(int(x) + int(y))

#z = "this is all about string"
#print(z)

"""
3 - Accepting input from users in Python
"""
#name = input("What is your fullname\n")
#ip = input("What is your @ip addr \n")
#print("Welcome",name,"Your @ip addr is",ip)

#num1 = input("Enter number1\t")
#num2 = input("Enter number2\t")
#print(num1,num2)
#print('The result is',int(num1) * int(num2))

"""
4 - Operators in Python
"""

#print(2*2)
#print(6//2)
#print(1+1)
#print(3-1)
#print(2/3)
#print(2//3)
#print(5%2)
#x = 2
#y = 3
#z = 1
#print(x+y*x-y)
#print((x+y)*x-y)
#print(45-71/45*2-3)

"""
5 - If statement
"""

#ip = 25
#if(ip==25):
#    print("You are a member of the IT department")

#a = 5
#b = 8
#c = 7

#d = a*c
#if(b==8):
#    print('The result is',d)
#    print("Welcome")

"""
6 - If else statement
"""

#ip = 75

#if(ip < 75):
#    print("You are a member of the IT department")
#else:
#    print("You are a member of the Research department")

#a = 6
#b = 4
#c = 7
#d = a*c

#if(b == 12):
#    print(d)

#else:
#    print(c-a)

"""
7 - elif statement in Python
"""

#ip = 1000

#if(ip == 75):
#    print("You are a member of the IT department")

#elif(ip == 100):
#    print("You are a member of the Research department")

#elif(ip == 200):
#    print("You are a member of the Communication department")

#elif(ip > 30000):
#    print("You are a member of the AI department")

#else:
#    print("You are a member of the ML department")


"""
8 - For loop in Python
"""

#for i in range(5):
#    print("Welcome to Python")
#    #print(i)

#for i in range(5,11):
#    print(i)

#for i in range(3,15,3):
#    print(i)

#name = 'Hi'
#for i in range(4):
#    print(name)


#number = 0
#for i in range(5):
#    number = number + i
#    print(number)

"""
9 - While loop in Python
"""

#for i in range(5):
#    print(i)

#i = 0
#while(i<5):
#    print(i)
#    i = i+1

#i = 0
#while(i<5):
#    print("Hello World")

#i = 0
#while(i<5):
#    print(i)
#    i = i+1

"""
10 - Break Statement in Python
"""

#i = 1
#while(i <= 100):
#    print(i)
#    if(i == 7):
#        break
#    i = i+1

#while 1:
#    lname = input("Please enter your lname...\t")
#    if(lname=='pat'):
#        break


#i = 1
#while (i == 1):
#    fname = input("Please enter your fname...\t")
#    if(fname=='thenavigo'):
#        break

"""
11 - Continue Statement
"""

#i = 1
#while(i < 100):
#    i = i+1
#    if(i <= 50):
#        continue
#    print(i)


"""
12 - String properties in Python
"""

#a = 'Hello'
#b = "World"
#c = 55
#d = 'Hello World'

#print(a)
#print(b)
#print(a+' '+b)
#print(a,b)
#print(a+' '+str(c))
#print(a.upper())
#print(b.lower())
#print(len(a))
#print(b[1])
#print(d[5])
#print(d[:5])
#print(d[1:5])
#print(d[3:9])
#print(d*10)

"""
13 - List[] in Python
"""

#list1 = [54, 12, 76, 11, 35]
#print(list1[2])
#print(len(list1))
#print(list1[:2])
#print(list1[1:4])

#list2 = ['World', 'Hello', 'Hi', 'Pat']
#print(list1,list2)
#print(list2[0])
#print(list2[-2])
#print(list1[-4])

#list3 = ['Hello', 'World', 56, 78, 700]
#print(list3)
#print(list3[-1])

"""
14 - List [] methods in Python
"""

#a = ['Hi', 56, 'World', 56, 'Pat', 56, 34, 189]
#for i in a:
#    print(i)

#a.append('Hello')
#a.append(78)
#a.append(('Thenavigo', 6, 4, 'Store'))
#print(a)
#a.remove('Hello')
#print(a)
#print(a.index('Hi'))
#print(a)
#print(a.reverse())
#print(a.pop())
#print(a.pop(1))
#print(a.count('World'))
#print(a.count(56))
#print(dir())

"""
15 - Tuples in Python
"""

#b = (77, 'Hi', 'World', 68, 90)
#print(b.__add__('Hello'))
#print(b.remove())
#print(b.count(68))
#print(b.index(77))
#print([2])

"""
16 - Dictionaries in Python
"""

#d = {'Hi':77, 'Hello':56, 'World':86, 'Thenavigo':64}
#print(d)
#print(d['Thenavigo'])
#d['Pat'] = 450
#print(d)
#del d['Hello']
#print(d)

#x = [1,2,3,4,5,6]
#y = [0,9,8,7,6,5]

#dict = {'x':[1,2,3,4,5,6], 'y':[0,9,8,7,6,5]}
#print(dict)

"""
17 - Functions in Python
"""

#Function definition begins with "def".
#Function has a name and arguments

#def get_final_answer(filename):
    #Documentation String
    #line1
    #line2
    #The keyword return indicates the value to be sent back to the caller
    #return total_counter

#t = "The answer is" #t bound to a string
#y = 54 #y bound to an integer
#print (t,y)

#def myfun (x,y,z):
#    return x * y * z
#print(myfun(4,5,2))

#def myfun (n, t=7, h="Hi"):
#    return n + t
#print(myfun(3,7,'Hello'))
#print(myfun(8,6))
#print(myfun(9))

#def square(x): return x*x
#def applier(q,x): return q(x)
#print(applier(square, 7))

#print(max(67,23,98,345,71,87,54))
#print(min(67,23,98,345,71,87,54))
#print(dir(__builtins__))
#print(help(pow))
#print(help(max))


"""
18 - Modules in Python
"""

#import math
#print(math.sqrt(7))

#print(help("modules"))
#print(help(math))



"""
19 - User define functions in Python
"""

#def example():
#    return "This is our function"
#print(example())

#def userinput():
#    user = input("Please, enter your fname...\t")
#    return user
#print(userinput())


#def addition():
#    num1 = int(input("Enter first number: \t"))
#    num2 = int(input("Enter Second number: \t"))
#    return num1 + num2
#print(addition())


"""
20 - User define functions with argument
"""

#def addition(num1, num2):
#    return num1 + num2
#print(addition(2,7))


"""
21 - Round of Modules and Functions
"""

#import Operations

#print(Operations.add(10, 2))
#print(Operations.subtract(10, 2))
#print(Operations.mul(10, 2))
#print(Operations.div(10, 2))



"""
22 - Time Module in Python
"""

#import time
#print(time.time())
#print(time.localtime(1704827819.8297575))


"""
23 - Example of Time module in Python
"""

import time

print(time.time())

login1 = time.time()
Msg1 = time.time()
Logout1 = time.time()

Login2 = time.localtime(login1)
Msg2 = time.localtime(Msg1)
Logout2 = time.localtime(Logout1)

Login = time.asctime(Login2)
Msg = time.asctime(Msg2)
Logout = time.asctime(Logout2)

print(Login)
print(Msg)
print(Logout)