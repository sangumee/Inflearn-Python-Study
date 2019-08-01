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

# Logical Operator (Important)
# and, or, not
a = 75
b = 40
c = 10
print('and : ', a > b and b > c)  # a>b>c
print('or : ', a > b or b > c)
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)

# Arithmetic, Relation, Logical Priority
# Arithmetic > Relation > Logical Priority
print('e1 : ', 3+12 > 7+3)
print('e2 : ', 5+10*3 > 7+3*20)
print('e3 : ', 5+10 > 3 and 7+3 == 10)
print('e4 : ', 5+10 > 0 and not 7+3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

# Ex5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('Admin Connected')

if id2 == 'admin' and grade == 'platinum':
    print('Super User!')

# Ex6
# Multiple Contional Statement
num = 90
if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade: B')
elif num >= 70:
    print('Grade : C')
else:
    print('Not Passed')

# Nested conditional statements
# Ex7
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('scholarship 100%')
    elif total >= 80:
        print('scholarship 80%')
    else:
        print('scholarship 50%')
else:
    print('No scholarship')

# in, not in
q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name": "Lee", "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Seoul" in e.values())
