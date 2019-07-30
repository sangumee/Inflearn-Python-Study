# Chapter03_04
# Python Tuple
# Should know about difference with List
# Cannot modify or remove

# Declaring Tuple

a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# Indexing
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# Cannot Modify
# d[0] = 1500 # ERROR

# Slicing
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# Calcuate Tuple
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# Tuple Function
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# Packing & Unpacking

# Packing
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# Unpacking 1
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x1))
print(x1, x2, x3, x4)

# Packing & Unpacking 2
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)