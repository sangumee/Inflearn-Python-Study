# Chapter04_02
# Python For Statement

# for in <collection>
#   <loop body>

for v1 in range(10):  # 0~9
    print('v1 is : ', v1)
print()

for v2 in range(1, 11):  # 1~10
    print('v2 is : ', v2)
print()

for v3 in range(1, 11, 2):  # 1~10, jump 2
    print('v3 is : ', v3)
print()

# Add 1 ~ 1000
sum1 = 0

for v in range(1, 1001):
    sum1 += v
print('1 ~ 1000 SUM : ', sum1)

print('1 ~ 1000 SUM : ', sum(range(1, 1001)))
print('1 ~ 1000 Multiples of 4 SUM : ', sum(range(4, 1001, 4)))

# Iterables Data Type
# String, List, Tuple, Set, Dictionary
# iterables return Function : range, reversed, enumerate, filter, map, zip

# Ex1
names = ['kim', 'Park', 'CHo', 'Lee', 'Choi', 'Yoo']


for name in names:
    print('You are : ', name)

# Ex2
lotto_numbers = [11, 19, 21, 28, 36, 27]

for n in lotto_numbers:
    print('Current Number : ', n)

# Ex3
word = "Beautiful"
for s in word:
    print('word : ', s)

# Ex4
my_info = {
    "name": 'Lee',
    "age": '26',
    "City": "Ulsan"
}

for key in my_info:
    print('key : ', my_info[key])

for v in my_info.values():
    print('value : ', v)

# Ex5
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found!')
        break
    else:
        print('Not Found : ', num)

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print('CURRENT TYPE : ', v, type(v))
    print('multiply by 2', v*2)
    print(True*3)

# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 3:
        print('Found : 3')
        break
else:
    print('Not Found : 3')

# Print Multiplication table

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()

# Conversion Example

name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))  # No Sequence
