# Chapter08_02
# Python External Functions
# Frequently used during actual program development
# Type : sys, pickle, shutil, temfile, time, random ...

# Ex1
import pickle
import sys
print(sys.argv)

# Ex2 (Exit)
# sys.exit()

# Ex3 Find Python Package path
print(sys.path)

# pkckle : object file write

# Ex4 (Write)
f = open('test.obj', 'wb')
obj = {1: 'python', 2: 'study', 3: 'basic'}
pickle.dump(obj, f)
f.close()

# Ex5 (Read)
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()
