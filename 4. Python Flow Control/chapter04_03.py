# Chapter04_03
# Python Iteration
# While

# while <expr>:
#   <statement(s)>

# Ex1

n = 5
while n > 0:
    n = n-1
    print(n)

# Ex2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

# Ex3
# break, continue

m = 5
while m > 0:
    m -= 1
    if m == 2:
        break
    print(m)
print('Loop Ended.')

# if overlap
i = 1
while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1

# While - else Statement
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')

# Ex7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'
i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list')

# Infinite Iteration
# while True:
#   print('FOO')

# Ex8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())
