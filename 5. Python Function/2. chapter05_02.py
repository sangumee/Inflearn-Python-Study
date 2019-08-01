# Chapter05_02
# Python User Input
# How to use Input in Python
# Bastic Type (str)

# Ex1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company Name : ")

print(name, grade, company)

# Ex2
number = input('Enter Number : ')
name = input('Enter Name : ')

print('type of Number', type(number), number)
print('type of Name', type(name), name)

# Ex3 (Calculate)
first_number = int(input('Enter number1 : '))
second_number = int(input('Enter number2 : '))
total = first_number+second_number
print('first_number + second_number is ', total)

# Ex4
float_number = float(input('Enter a float Number : '))
print('input float :', float_number)
print('input type : ', type(float_number))

# Ex5
print("FirstName - {0}, LastName - {1}".format(
    input('Enter first Name : '), input('Enter second name : ')))
