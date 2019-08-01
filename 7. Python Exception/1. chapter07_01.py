# Chapter07_01
# Python Exception Handling
# Exception Type
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...

# There is no grammatical exception, but the exception that occurs in the code execution process (step) is also important

# 1. Exceptions MUST be handled
# 2. Exceptions always leave.
# 3. The exception is thrown.
# 4. Ignore exceptions

# SyntaxError
# print('error)
# print('error'))
# if True
#     pass

# NameError
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
# print(100/0)

# IndexError
# x = [50, 70, 90]
# print(x[1])
# print(x[5])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# KeyError
# dic = {'name': 'Lee', 'Age': 41, 'City': 'Ulsan'}
# print(dic['hobby'])
# print(dic.get('hobby'))

# Program development assuming no exceptions -> Exception handling recommended at runtime exceptions (EAFP)

# AttributeError : Unknown property in Modele & Class
# import time
# print(time.time2())

# ValueError
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError
# f = open('test.txt')

# TypeError : If you perform an operation that does not match the data type
# x = [1, 2]
# y = (1, 2)
# z = 'test'

# print(x+y)
# print(x+z)
# print(y+z)

# print(x+list(y))
# print(x+list(z))

# Exception Handling
# try : Execute code that may cause an error
# except ErrorName1 : Possible with multiple
# except ErrorName2 :
# else : if try block missing
# finally : always execute

# name = ['Kim', 'Lee', 'Park']

# Ex1
# try:
#     z = 'Kim'
#     x = name.index(z)
#     print('{} Found it {} in name'.format(z, x+1))
# except ValueError:
#     print('Not found it - Occurred ValueError!')
# else:
#     print('Ok!')
# print()

# Ex2
# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('{} Found it {} in name'.format(z, x+1))
# except:
#     print('Not found it - Occurred ValueError!')
# else:
#     print('Ok!')
# print()

# Ex3
# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('{} Found it {} in name'.format(z, x+1))
# except Exception as e:
#     print(e)
#     print('Not found it - Occurred ValueError!')
# else:
#     print('Ok!')
# finally:
#     print('Ok! Finally')
# print()

# Ex4
# Create Exception : raise

# try:
#     a = 'Park'
#     if a == 'Kim':
#         print('Ok! Pass')
#     else:
#         raise ValueError
# except ValueError:
#     print('Occurred Exception')
# else:
#     print('Ok! else')
