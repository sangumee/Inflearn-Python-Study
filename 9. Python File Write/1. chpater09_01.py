# Chapter09_01
# File Write and Read

# Read Mode : r, Write Mode : w, Add Mode : a, Text Mode : t, Binary Mode : b
# Path ('../, ./')

# File Read

# Ex1
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')
# Check Property
print(dir(f))
# Check Encoding
print(f.encoding)
print(f.name)
print(f.mode)
cts = f.read()
print(cts)

# Must be close
f.close()

# Ex2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
# Automatically close()
print()

# Ex3
# read() : Read All, read(10) : 10Byte
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0, 0)    # Go to First
    c = f.read(20)
    print(c)
print()

# Ex4
# readline : read line by line
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

# Ex5
# readlines : Read all and save with line with lists
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')
print()

# File Write

# Ex1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love Python \n')

# Ex2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love Python2 \n')

# Ex3
# writelines : list -> file
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# Ex4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
