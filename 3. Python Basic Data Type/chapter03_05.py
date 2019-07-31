# Chapter03_05
# Python Dictionary
# Most Use, Looks like JSON Data
# No Sequence, Key Duplication are not allowed
# But Modifying and Deleting are okay

# Declaration
a = {'name': 'Kim',
     'phone': '01099999999',
     'birth': '940614'
     }
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'NiceMan',
    'City': 'Ulsan',
    'Age': '26',
    'Grade': 'A',
    'Status': True
}

e = dict([
    ('Name', 'NiceMan'),
    ('City', 'Ulsan'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

# Best Way
f = dict(
    Name='NiceMan',
    City='Ulsan',
    Age=26,
    Grade='A',
    Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# Print
print('a - ', a['name'])
# If key ia missing print 'NONE' Best Way to handling error
print('a - ', a.get('name'))
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# Add Dictionary
a['address'] = 'ulsan'  # Add address in 'a'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# Check DIctionary Length
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items : can use in iteration (__iter__)
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('a - ', list(a.values()))
print('b - ', list(b.values()))
print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('a - ', list(a.items()))
print('b - ', list(b.items()))
print()

# pop
print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)
print()

# Randomly remove item in dictionary
print('f - ', f.popitem())
print('f - ', f)
print()

# Check Key Exists
print('a - ', 'birth' in a)
print('d - ', 'City' in d)

# Modifying
a['test'] = 'test_dict'
print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth='184756')
print('a - ', a)
temp = {'address': 'Busan'}
a.update(temp)
print('a - ', a)
