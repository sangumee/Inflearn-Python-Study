# Chapter06_01
# Data Type SET
# No Sequence
# No Duplication

# Declaration
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.1459}

# Print
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# Tuple Conversion (set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# List Conversion (set -> list)
l = list(c)
l2 = list(e)
print('l - ', l)
print('l2 - ', l2)

# Length
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# Set Data Type Use
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))

print('s1 | s2 :', s1 | s2)
print('s1 | s2 :', s1.union(s2))

print('s1 - s2 :', s1 - s2)
print('s1 - s2 :', s1.difference(s2))

# Duplication Check
print('s1 & s2 :', s1.isdisjoint(s2))

# Verify subsets
print('subset : ', s1.issubset(s2))
print('superset : ', s1.issuperset(s2))

# Add data and Remove
s1 = set([1, 2, 3, 4])

# Add
s1.add(5)
print('s1 - ', s1)
# Remove
s1.remove(2)
print('s1 - ', s1)
# Discard, Ignore Error
s1.discard(3)
s1.discard(7)
print('s1 - ', s1)

# Remove all
s1.clear()
print('s1 - ', s1)
