class MyClass:
    x = 3 
    y = 1
    def my_method(self): #self = a
        print(self.x)  #a.x
        print(self.y)  #a.y
        print("Hello World")
    def hello(self,u): #self = a, u =5
        print(u)
    def add(self,i,o):
        return i+o


a = MyClass()  
a.my_method()
b  = MyClass()
print(b.x)
print(b.y)
b.my_method()

a.x = 50
b.x = 100

print(a.x)
print(b.x)


print(type(a))
a.hello("puzan")
x = 5
print(type(x))

