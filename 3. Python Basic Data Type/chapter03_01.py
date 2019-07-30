# Chapter03_01
# Number

# Python Support Data Type
'''
int
float
complex
bool
str
list
tuple
set
dict
'''

# Data Type
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.4 # 10 == 10.0 -> False
int_v = 7
list = [str1, str2]
print(list)
dict = {
    'name': 'Python',
    'version':3.7
}
tuple = (7, 8, 9)
set = {3, 5, 7}

# Print Data Type
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

# Number Operator
'''
+
-
*
/
//
%
abs(x)
pow(x, y)
'''

# Integer
i = 77
i2 = -14
big_int = 92923491284719082748917298471872

# Print Integer
print(i)
print(i2)
print(big_int)

# Float Print
f = 0.99999
f2 = 3.14592
f3 = -3.9
f4 = 3/9

print(f)
print(f2)
print(f3)
print(f4)
print()

# Calculate
i1= 39
i2 = 939
big_int1 = 77777777771982749812749817298938
big_int2 = 3093481089370489172098471024701928309128
f1 = 1.234
f2 = 3.939

# + 
print(">>>>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

# 8
print(">>>>>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

# Type Conversion
a = 3.
b = 6
c = .7
d = 12.7

# Print Type
print(type(a), type(b), type(c), type(d))

print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1 False : 0
print(float(False)) # 0.0
print(complex(3))
print(complex('3')) # String -> Number
print(complex(False))

# Numerical computation function
print(abs(-7))

x, y = divmod(100, 8)
print(x, y)
print(pow(5,3), 5 ** 3)

# External Module
import math

print(math.ceil(5.1)) # The smallest integer in the number x and above.
print(math.pi)