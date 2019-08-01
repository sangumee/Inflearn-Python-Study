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
