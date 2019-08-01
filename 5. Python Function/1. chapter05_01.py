# Chapter05_01
# Python Function
# Python Function and Lamda

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
