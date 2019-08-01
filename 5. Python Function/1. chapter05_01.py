# Chapter05_01
# Python Function
# Python Function and lambda

# How to defeine Function
# def function_name(parameter):
#   code

# Ex1


def first_func(w):
    print('Hello, ', w)


word = 'Goodboy'
first_func(word)


# Ex2
def return_func(w1):
    value = 'Hello, ' + str(w1)
    return value


x = return_func('Goodboy2')
print(x)

# Ex3 Multiple returns


def func_mul(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return y1, y2, y3


x, y, z = func_mul(10)
print(x, y, z)


def func_mul2(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return (y1, y2, y3)


q = func_mul2(20)
print(type(q), q, list(q))

# Return List


def func_mul3(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return [y1, y2, y3]


p = func_mul3(30)
print(type(p), p, set(p))


def func_mul4(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return {'v1': y1, 'v2': y2, 'v3': y3}


d = func_mul4(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())

# Important
# *args, **kwargs
# *args(Unpacking) Tuple


def args_func(*args):    # No problem with arguments
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('------')


args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **kwargs(Unpacking) Dictionary


def kwargs_func(**kwargs):  # No problem with arguments
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('------')


kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Kim')

# Whole mix


def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)


example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)

# Nested function


def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In func')
    func_in_func(num+100)


nested_func(100)
# func_in_func (Cannot use)

# lambda Example
# Memory savings, readability improvements, code snippets
# Function create object -> allocate resources (memory)
# Lambda immediately executes function (Heap initialization) -> memory initialization
# Reduced readability


# def mul_func(x, y):
#    return x*y


# lambda x, y: x*y

def mul_func(x, y):
    return x*y


print(mul_func(10, 50))
mul_func_var = mul_func
print(mul_func_var(20, 50))


# lambda_mul_func=lambda x,y:x*y
# print(lambda_mul_func(50, 50))

def func_final(x, y, func):
    print(x*y*func(100, 100))


func_final(10, 20, lambda x, y: x*y)
