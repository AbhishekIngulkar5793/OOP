"""
Types of Method in OOP
1. Instance method:
- A method with self is an instance method.
- It/s an instance because we can access and call
  it anywhere using object and self reference.
-------------------------------------------------
class Sample:
    def __int__(self):
        print('init Method')
    def show(self):
        print('Show method')
        #self.show() # recursion
    def other(self):
        self.show()
        self.__int__()

s = Sample()
s.show()
s.other()

output:

Show method
Show method
init Method

Process finished with exit code 0
----------------------------------------------
class Movie:
    def sholey(self):
        print('Gabbar')
    def kantara(self):
        print('Shiva')
    def blockbuster(self):
        self.kantara()
        self.sholey()

m = Movie()
m.blockbuster()

#m.kantara()
#m.sholey()

output:
Shiva
Gabbar


Process finished with exit code 0
------------------------------------------------
Q. Can we supply arguments to the methods?
--> Yes, see below example.

----------------------------------------
class Test:
    def __int__(self, name, age):
        # converting local to instance var
        self.n = name
        self.a = age
    def display(self, nm, age):
        print('Your name is:', self.n)
        print('Your age is:', self.a)
        print('Your name is:', nm)
        print('Your age is:', age)

t = Test()
t.display('Sham', 22)
----------------------------------------------
2. Static method
- A method without self is known as static method.
- we can supply arguments to this method those
  will be constunt for the same method.
- So we cant share them in other instance method
  using self.
- A normal method become a static method using
  @staticmethod decorator
--------------------------------------
class Test:

    @staticmethod
    def add(x, y):
        print('Addition:', x+y)

t = Test()
t.add(10, 20)

output:
Addition: 30

Process finished with exit code 0
------------------------------------------------
class Test:

    @staticmethod
    def add(x, y):
        print('Addition:', x + y)

    def call(self):
        self.add(20, 40)

t = Test()
t.add(10, 20)
t.call()

output:
Addition: 30
Addition: 60

Process finished with exit code 0
==========================================
3. class method:
- It is used to access class level variable or static vars
- In this class is used instead of self
- @classmethod decorator is used to make a normal method
  as a class method.
------------------------------------------------
class Sample:
    x = 500
    y = 600

    def display(self):
        self.a = 10
        self.b = 20
        self.x = 5
        self.y = 6
        print('Display:', self.x, self.y)
    # to access static vars. use a class method
    @classmethod
    def access(cls):
        print('Access:', cls.x, cls.y)
        cls.x = 1000

s = Sample()
s.display()
print(s.__dict__)
s.access()
print(s.x)
print(Sample.x)

output:

Display: 5 6
{'a': 10, 'b': 20, 'x': 5, 'y': 6}
Access: 500 600
5
1000

Process finished with exit code 0
-----------------------------------------

"""


