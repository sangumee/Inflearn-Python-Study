# Chapter08_02
# Python External Functions
# Frequently used during actual program development
# Type : sys, pickle, shutil, temfile, time, random ...

# Ex1
import webbrowser
import random
import time
import os
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

# os : Environment Variable, Directory(File) Process, OS Process
# mkdir, rmdir (Remove when if empty), rename

# Ex6
print(os.environ)
print(os.environ["USERNAME"])

# Ex7 (Current Path)
print(os.getcwd())

# time : time process

# Ex8
print(time.time())

# Ex9
print(time.localtime(time.time()))

# Ex10
print(time.ctime())

# Ex11
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# Ex12
# for i in range(5):
#     print(i)
#     time.sleep(1)

# random

# Ex13
print(random.random())  # 0~1 Floadt

# Ex14
print(random.randint(1, 45))
print(random.randrange(1, 45))

# Ex15 Shuffle
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

# Ex16 : Choose Randomly
c = random.choice(d)
print(c)

# webbrowser : Execute Web Browser
webbrowser.open('https://writingdeveloper.tistory.com')
webbrowser.open_new('https://writingdeveloper.tistory.com')
