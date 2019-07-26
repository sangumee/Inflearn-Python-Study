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
print('{1} {0}'.format('one', 'two'))