# Chapter03_03
# Python List
# Data Structure

# List Data Type

# Declaring List
a = []
b = list()
c = [70, 75, 80, 85]    #len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14139]

# Indexing
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', list(e[-1][1]))

# Slicing
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', list(e[-1][1:3]))

# List Calculation
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# Compare Values
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity (id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

# Modify List
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] # Delete
print('c - ', c)
print()

# List Functions
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a)
# del a[6]
a.remove(10)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# Remove, Pop, del

# Iteration
while a:
    data = a.pop()
    print(data)