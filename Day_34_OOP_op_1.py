"""
share = [98, 56, 78]
companies = ['infy', 'ibm', 'tcs']
import matplotlib.pyplot as plt
plt.bar(companies,share)
plt.show()
---------------------------------------
Advance Python
Object Oriented Programming:
In python Everything is an object
Object is an entity which exists physically
in an environment
-------------------------------------------
s = 'Python'
print(id(s))
print(id('Python'))
print(type(s))
-------------------------------------
output:
1953135618792
1953135618792
<class 'str'>

Process finished with exit code 0
=================================================
object : It is an instance of a class

Q.what is a class???
--> class is a container which contains two things,
-which are:     properties (Attributes/Variables)
                            +
                Behaviour (Actions/Methods/Operations)

- class is a template, a structure, a blueprint
  which is composed of two things

- class = variables + methods

#Example of a mobile (Object)

class Mobile:

    properties: RAM, Memory, Camera, BT,..
    Behaviour: Power on, Restart, Calling, Messaging

Using a class we can create n number of objects
---------------------------------------------------
s = 'Py'

print(type(s))
output:
<class 'str'>

Process finished with exit code 0
===============================================

Example:
=========================================
class MobileStore:
    m1 = 'Vivo'
    m2 = 'Realme'
    m3 = 'iphone'

    def price(self):
        if self.m1 == 'Vivo':
            print('Price is:', 25000)
# Memory allocation is needed after declaration of a class
MobileStore().price()
# calling of a class will allocate a memory
# Q. Difference between function and method?


# print() #its a function
# [].pop() #its a method

"""


