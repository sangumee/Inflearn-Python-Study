# Chapter04_01
# Python Control Statement
# IF

# Basic
print(type(True))   # Nonzero, String
print(type(False))  # 0, Empty List & String..

# Ex1
if True:
    print('Good')

if False:
    print('Bad')

# Ex2
if False:
    print('Bad!')
else:
    print('Good!')

# Relational Operators

# >, >=, <. <=, ==, !=
x = 15
y = 10
# If Same
print(x == y)
# If Different
print(x != y)
# Check
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

# Ex3
city = ""
if city:
    print('You are in:', city)
else:
    print('Please enter your city')

# Ex4
city2 = "Seoul"
if city2:
    print('You are in:', city2)
else:
    print('Please enter your city')
