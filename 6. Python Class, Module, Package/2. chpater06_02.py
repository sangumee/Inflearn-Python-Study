# Chapter06_02
# Python Module
# Module : A collection of Python components, including functions, variables, and classes.


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


def power(x, y):
    return x**y


print('-' * 15)
print('Called! Inner!')
print(add(5, 5))
print(subtract(15, 5))
print(multiply(5, 5))
print(divide(10, 2))
print(power(5, 3))


if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(divide(10,2))
    print(power(5,3))
    print('-' * 15)