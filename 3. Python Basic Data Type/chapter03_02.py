# Chapter03_02
# Python String

# Create String
str1 = 'I am Python'
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# Empty String
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# Use Escape String
print("I'm Boy")
print('I\'m Boy')
print('a \t b')
print('a \n b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What \'s on TV?'
print(escape_str2)

# Tab, Line Change
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s1 = r'D:\Python\test'
print(raw_s1)

# Multi Line Input
multi_str = \
'''
String
Multi Line
TEST
'''

print(multi_str)

# String Calcuation
str_o1 = 'python'
str_o2 = 'Apple'
str_o3 = 'How are you doing?'
str_o4 = 'Seoul Deajeon Busan Ulsan'

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o2)
print('P' not in str_o2)

# String Type Change
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# String Function (upper, isalnum, startswith, count, endswith, isalpha...)

print('Capitalize ', str_o1.capitalize())
print('endswith? : ', str_o2.endswith('e'))
print('replace', str_o1.replace('thon', ' Good'))
print('sorted : ', sorted(str_o1))
print('split', str_o4.split(' '))

# Repeated String (Sequence)
im_str = 'Gooe Boy!'

print(dir(im_str)) # __iter__

# Output
for i in im_str:
    print(i)

# Slicing
str_sl = 'Nice Python'

print(len(str_sl))  # String Length
# Slicing Practice
print(str_sl[0:3])  # 0 1 2
print(str_sl[5:]) # [5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])

# ASCII Code or UNICODE
a = 'z'

print(ord(a))
print(chr(122))