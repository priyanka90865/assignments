#different data types

#numarical data types

#1.integer >>>> a number without decimal values
num = 10
a = 1
b = -22
print(type(num),type(a),type(b))

#2.float >>>> a numer with a decimal values
c = 10.5
d = 8.88
e = 4.44
print(type(c),type(d),type(e))

#3.complex >>>> we have  real number and  imaginary number
a = 7+4j
v = 2+3j
print(type(a),type(v))
print(a)

#strings >>>> collection of characters represent in between '',"",""" """
name = "sai"
print(name)
a = 'animal'
print(type(name))
print(type(a))
abc = """ hello world 
python is a very easy language"""
print(abc)
print(type(abc))

#list >>>> collection of all the data types and store in a single variable 
details = ["abhay",88,55.55,True]
print(details)
print(type(details))

#tuple >>>> collection of all the data types and store in a single variable,immutable
t = (20,40,60,'ram',66.8,True)
print(t)
print(type(t))

#dictionary >>>> unordered collection of keys and values
d = {}
print(type(d))
d={1:"tejs",2:'abhay','marks':88.8}
print(d[1])
print(d)

#set  >>>> unorderd collection of unique items
s={1,2,3,4,5,6,7,8,9,1,2,3,4,}
print(s)
print(type(s))

#boolean  >>>> represents true,false
print(30>40)
print(40>30)

import keyword

print(keyword.kwlist)


#operators in python

#arthmetic operators
#addition
print(10+20)
print(50+30)

#subtraction
print(30-10)
print(40-20)

#multiplication
print(10*5)
print(20*3)

#module 
print(10%2)

#floor division
print(10//2)

#division
print(10/2)

#exponentiation
print(10**2)


#relational operators#
# <, >, <=,>=,==,!=

print(10<20)
print(10>20)
print(10<=20)
print(10>=20)
print(10==20)
print(10!=20)

#logical operators
#and ,or ,not
x=10>20
Y=20>10

print(x and y) # return true if both condiyions are true
x=10>20
y=20>10
print(x or y) #return true if any one condition is true
x=10>20
y=20>10
print( not x) #return true if the condition is false
print( not y)

#identity operators
#bitwise operators
#membership operators
#assignment operators

