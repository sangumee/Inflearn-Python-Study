# Python Basic

print('Python Start')   # Most Used!!
print("Python Start")
print('''Python Start''')
print("""Python Start""")

print() # Empty Space

# Separator Option
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('Python', 'google.com', sep='@')

print()

# End Option
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# File Option
import sys
print('Learn Python', file=sys.stdout)
print()

# Use Format (d : 3, s : 'python', f : 3.1444562)
# s : String

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two')) # Comfortable using method
print('{1} {0}'.format('one', 'two')) # Sequence

print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^>10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # cut
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%f' % (3.1494294242))
print('{:f}'.format(3.1494294242))

print('%06.2f' % (3.1494294242))