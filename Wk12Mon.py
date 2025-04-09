#Short hand conditional

a = 1
b = 3

c = print("a") if a > b else print("b")

#Match

#functions
def my_function(country = "Norway"):
    print("I am from " + country)
    
my_function("Venezuela")

def printVoting(msg = "Current Message"):
    print(msg)
    
printVoting("Vote again")
printVoting()

#Positional-onloy Arguments
def myfunction2(x, /):
    print(x)
    
myfunction2(1)

#Combine Positional-Only and Keyword-Only
def my_function3(a, b, /, *, c, d):
  print(a + b + c + d)

my_function3(5, 6, c = 7, d = 8)

#Lamba
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

#Objects and Classes
class MyClass:
    x = 5

class Person:
    def __init__(self, name, age):
       self.name = name 
       self.age = age
       
p1 = Person("John", 36)
    
print(p1.name)
print(p1.age)
    
print(p1)

#Practice
print("=============================================================")

#ShoppinCart Application
