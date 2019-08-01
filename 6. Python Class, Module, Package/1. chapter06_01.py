# Chapter06_01
# Python Class
# OOP (Object-oriented programming), Self, Instance Method, Instance Variable

# Understanding difference with Class and Instance
# Namespace: Space saved when instantiating an object
# Class variables: Direct access and share
# Instance variables: exist separately for each object

# Ex1


class Dog:    # object Inheritance
    # Class Property
    species = 'firstdog'

    # Class reset/ Instance property
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Class Information
print(Dog)

# Instance
a = Dog('Mikky', 2)
b = Dog('baby', 3)

# Compare
print(a == b, id(a), id(b))

# Namespace
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# Check Instance property
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# Ex2
# Understanding self


class SelfTest:
    def func1(self):
        print('Func1 called', self)

    def func2(self):
        print(id(self))
        print('Func2 called')


f = SelfTest()
# print(dir(f))
print(id(f))

# f.func1() # Exception
f.func2()
SelfTest.func1('app')
# SelfTest.func2(f) # Exception
SelfTest.func2(f)

# Ex3
# Class Variable, Instance Variable


class Warehouse:
    # Class Variable
    stock_num = 0  # Stock

    def __init__(self, name):
        # Instance Variable
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('After', Warehouse.__dict__)

# Ex4


class Dog1:    # object Inheritance
    # Class Property
    species = 'firstdog'

    # Class reset/ Instance property
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)


# Instance
c = Dog1('july', 4)
d = Dog1('Marry', 10)
# Method Call
print(c.info())
print(d.info())
# Method Call
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))
