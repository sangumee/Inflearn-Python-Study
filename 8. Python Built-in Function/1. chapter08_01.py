# Chapter08_01
# Python Built-in Functions
# str(), int(), tuple()

# Absolute value
# abs()

print(abs(-3))

# all : checks iterable property (True, False)
print(all([1, 2, 3]))   # Must have all True Values
print(any([1, 2, 0]))   # or

# chr : ASCII -> String , ord : String -> ASCII
print(chr(67))
print(ord('C'))

# enumerate : Index + create Iterable Object
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i+1, name)

# filter : Extracts a repeatable object element that matches the specified function conditions


def conv_pos(x):
    return abs(x) > 2


print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2,  [1, -3, 2, 0, -5, 6])))

# id : Returns the address value (reference) of an object
print(id(int(5)))
print(id(4))

# len : Length
print(len('abcdefg'))
print(len([1, 2, 3, 4, 5, 6, 7]))

# max, min : Maximum, Minimum
print(max([1, 2, 3]))
print(max('Python Study'))

print(min([1, 2, 3]))
print(min('Python Study'))

# map : Extract repeatable object elements after executing a specified function


def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))
