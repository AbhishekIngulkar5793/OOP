"""
Object Oriented Programming Concepts
============================================
z = 300 # Global var.

class Sample:
    x = 100 # Static var/ Class level

    def m1(self):
        p = 400 # Local var.
        self.y = 200 # Instance var.

q = 500 # Global var.
----------------------------------------------------
We have total three reference variables -
1. self
2. Object
3. ClassName
========================================
class Bank:
    # static variables
    name = 'SBI'
    ifsc = 'SBI34566'

    def access(self):
        # using self
        print(self.name, self.ifsc)
        # using ClassName
        print(Bank.name, Bank.ifsc)

b = Bank()
b.access()
print(Bank.name, Bank.ifsc)


output:

SBI SBI34566
SBI SBI34566
SBI SBI34566

Process finished with exit code 0
-----------------------------------------
# global vars
name = 'SBI'
ifsc = 'SBI23456'

class Bank:

    def access(self):
        #using self
        print(name, ifsc)
        #using ClassName
        print(name, ifsc)
b = Bank()
b.access()
print(name, ifsc)

output:
SBI SBI23456
SBI SBI23456
SBI SBI23456

Process finished with exit code 0
=======================================
class Bank:

    def access(self):
        # local variables
        name = 'SBI'
        ifsc = 'SBI123'
        # no need of self/className to access
        print(name, ifsc)

b = Bank()
b.access()
# local variables are only available inside
# a method. We cant access them outside using
# object.
# inside using self
# inside and outside using ClassName

output:
SBI SBI123

Process finished with exit code 0
=======================================
class Bank:

   def access(self):
       Name = 'BOI' # local
       # Instance variables
       self.name = 'SBI'
       self.ifsc = 'SBI66778'
       print('Access:', self.name, self.ifsc, Name)
   def show(self):
       print('Show:', self.name, self.ifsc,)
       # Name is a local to access
       # hence wont be accessible


b = Bank()
b.access()
b.show()
print(b.name)
# outside name and ifsc will be available
# because of the instance var.

output:

Access: SBI SBI66778 BOI
Show: SBI SBI66778
SBI

Process finished with exit code 0
======================================
class Test:
    x = 500 # static var
    def m1(self):
        self.x = 100 # instance var

t = Test()
t.m1()
print(t.x)
# using ClassName

print(Test.x)
# ClassName will be a reference only for
# static var/Class Level vars

output:
100
500

Process finished with exit code 0
==================================
Constructor:
-Features
1. Constructor has same name as that of class name
2. It is used to allocate a memory
3. If you create a constructor object gets created
4. It instantiates  an object
5. When constructor gets called, object gets
   created automatically
6. We can call it n number of times
7. If we have 4 objects for ex. means
   constructor is needed to be called
   4 times Example:
class Test:
    pass
t1 = Test()
print(id(t1))
t2 = Test()
print(id(t2))
t3 = Test()
print(id(t3))
t4 = Test()
print(id(t4))

output:
2292306636528
2292306636304
2292307156776
2292306636584

Process finished with exit code 0

8. Constructor can be empty or we can supply
   arguments to it. This is possible using
   a magic/dender method.
def__init__(self):
    pass

   and this is internal implementation of a
   constructor
--------------------------------------
As constructor allocates a memory
We have constructor in python to
deallocate a memory
We can implement using another magic/dender
method,
def__del__(self):
    pass
=======================================
import time
class Test:
    def __int__(self):# Constructor method
            print('Constructor called')
            time.sleep(2)

    def __del__(self): # Autocalling
            print('Destructor called')
            time.sleep(2)
t1 = Test()
t2 = Test()
# When constructor gets called, then destructor
# gets called automatically.

output:
Destructor called
Destructor called

Process finished with exit code 0
====================================
class Sample:


    def __init__(self):
        print('Init of Sample class')


s = Sample()
print(id(s))

output:
Init of Sample class
2804937418064

Process finished with exit code 0
=======================================



"""


