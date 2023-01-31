"""
class: properties(variable) + behaviour(methods)

object: Its an instance of a class
------------------------------------------
class Cake:
    # a class with 2 variables and 2 methods
    suger = 1
    floor = 2

    def baking(self):
        print('Baking started')

    def icing(self):
        print('Icing process')

cake = Cake()
# cake is: an instance of a class Cake
# hence it is an object
# Cake() is: a constructor of a class cake

# lets create 2nd object
ice_cake = Cake()

# As per rule: a members of a class are not accessible
# outside the class
#print(suger)
#print(floor)
#baking()
#icing()

# Now if you want to access members outside
# then you must have to take the help of the
# object.
# So we have ice_cake object
# use it to access members

print(ice_cake.suger)
print(ice_cake.floor)
ice_cake.baking()
ice_cake.icing()

# as per requirement, we will decide from a class members
# which members to access
# use cake object
# its a normal process which don't require icing

print('-------------------------------------')

print(cake.suger)
print(cake.floor)
cake.baking()
----------------------------
output:
1
2
Baking started
Icing process
-------------------------------------
1
2
Baking started

Process finished with exit code 0
==================================================
self????
Q.  What is 'self' ??
-->
- It is a reference variable inside a class inside a method.
- self is available inside a method only
- It acts as a 'this pointer' in java.
- self points to the members of a method and to method itself.
--------------------------------------------

# P.S: Access x, y inside a method using self reference
# 2. Access x, y outside a class using object reference

class Sample:
    x = 100
    y = 200
    p = 77
    def m1(self):

        self.p = 70
        print('Inside:', self.x)
        print('Inside:', self.y)

s = Sample()
s.m1()

print('Out:', s.x)
print('Out:', s.y)
print(s.p)

output:

Inside: 100
Inside: 200
Out: 100
Out: 200
70

Process finished with exit code 0
-----------------------------------------------

# summery:
# Object acts as a reference variable outside a class.
# self acts as a reference variable inside a class.
-----------------------------------------------------
class Bank:
    pin = 1234
    ifsc = 'SBI5656'

b = Bank()
print(b.pin)
print(b.ifsc)

output:

1234
SBI5656

Process finished with exit code 0
-------------------------------------------------
g = 400 # global variable

class Bank:
    pin = 1234 # class level var. / static var.
    ifsc = 'SBI5656'
    # Now access pin and ifsc inside m1

    def m1(self):
        place = 'Pune' # local var.
        print(self.pin, self.ifsc, place, g)
        self.pin = 45454 # Instance var.

b = Bank()
b.m1()
print(g, b.pin)


output:
1234 SBI5656 Pune 400
400 45454

Process finished with exit code 0

# Global variable: Outside a class.
# Local variable: Inside a method.
# Static variable: Inside a class outside the method.
# Instance variable: Declared with self.

"""
age = eval(input('enter your age:'))


print(type(age))
for i in age:

    if i == 23:
        print(i)

