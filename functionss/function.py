
#program to greet 
def greet(name):   
    print(f"Hello {name} !" )
    print("Welcome to the world of Python")

greet("Ram")  
#program to add two numbers
def sum(a,b):
    add=a+b
    return add
b=sum(9,10)
print(b)
#-----------variables-------------#
#local variables and global variables
def my_func():
    x = 10  # x is local variable
    y = 20  # y is local variable
    print(" your local variables are: ", x, y)

x = 30  
my_func()
print("your global variable is  : ", x)
#--------------Functions Arguments---------------#
#Default Arguments
def default(a,b=10):
    mul=a*b
    return mul
c=default(5)
print("your product is ",c)
#keyword arguments
def keyword(a=10,b=10,c=50):
    mul=a*b*c
    return mul
f=keyword(c=5,b=1,a=5)
print("your product is ",f)
#args functions
def my_func(*args):
    print(args)
my_func(3,5,6,7,8,9,10,11,12,12,13)



