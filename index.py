#Variables and data types 
name = "Hira Irfan"
age = 21
is_student = True
print(name,  age, is_student)
print(type(name))
print(type(age))
print(type(is_student))


#Arithmetic operators 
x = 20
y = 6
print("Addition",  x+y)
print("Subtraction", x-y)
print("Multliplication", x*y)
print("Division", x/y)
print("Floor division", x//y)
print("Modulus", x%y)
print("Exponent", x**y)


#Assignment operators 
num = 10
num += 5
num *= 2
num -= 4
print(num)


#Comparision operators
a = 15
b = 12
print("a > b?", a > b)
print("a < b?", a < b)
print("a = b?", a == b)
print("a != b?", a != b)
print("a >= b?", a >= b)
print("a <= b?", a <= b)


#Logical operators
p = True
q = False
print("p and q is true?", p and q)
print("p or q is true?", p or q)
print("p not: ", not p)
print("q not: ", not q)


#Real-life example
one_notebook = 80
tot_price = 7 * one_notebook
my_balance = 600
if(my_balance >= tot_price):
    print("I can buy these notebooks")
else:
    print("I don't have enough money to buy these notebooks")


#Bonus task
num1 = int(input("Enter first number (x): "))
num2 = int(input("Enter second number (y): "))
print("x + y = ", num1 + num2)
print("x > y?", num1 > num2)



