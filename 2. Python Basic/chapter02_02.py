# Python Basic
# Python Variable

# Basic Variable
n = 700

# Output
print(n)
print(type(n))

# Simultaneous declaration
x = y = z = 700
print(x,y,z)

# Declaration
var = 75

# Redeclaration
var = 'Change Value'

# Output
print(var)
print(type(var))

# Object References
# Variable value assignment status
# 1. Create objects for type
# 2. Create Value
# 3 .Console Output

# Ex1)
print(300)
print(int(300))

# Ex2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
#m -> 777 <- n
print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

# id(identity) check : Check the eigenvalue of the object

m = 800
n = 655
print(id(m))
print(id(n))
print(id(m) == id(n)) # id value is False
print()

# The ID value is the same for the same variable value
m = 800
n = 800
z = 800
i = 800
print(id(m))
print(id(n))
print(id(m) == id(n)) # id value is False
print()

# Variable Declaration Method
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates -> Python Variable

# Permissible variable declaration Method
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# Python Keyword
"""
False	class	finally	is	return
None	continue	for	lambda	try
True	def	from	nonlocal	while
and	del	global	not	with
as	elif	if	or	yield
assert	else	import	pass	 
break	except	in	raise
"""