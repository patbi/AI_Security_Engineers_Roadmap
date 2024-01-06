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
for i in range(5):
    print("Welcome to Python")
    #print(i)

for i in range(5,11):
    print(i)

for i in range(3,15,3):
    print(i)

name = 'Hi'
for i in range(4):
    print(name)


number = 0
for i in range(5):
    number = number + i
    print(number)