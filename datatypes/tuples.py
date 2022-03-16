#creating a tuple
a = (1, 2, 3)
b = (4, 'five', 6.0)
c = ('seven', 8, 9.0,[10,11,12])
d = ()
e = 3, 4, 5
print(a)
print(b)
print(c)
print(d)
print(e)

#creating a tuple with one item
f = (1,)
print(f)
g = ('hello',)  
print(g)

#accessing elements in a tuple
print(a[0])
print(b[1])
print(c[3][1])
#negative indexing
print(a[-1])
print(b[-2])
print(c[-1][-1])

#slicing a tuple
print(a[0:2])
print(a[:])
print(b[1:])
print(c[3][1:3])

#change items of a tuple
#a[0] = 'one' #TypeError: 'tuple' object does not support item assignment
#print(a)

#but
c[3][1] = 'eleven'
print(c) 

#add elements to a tuple
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)

#remove elements from a tuple
t1 = (1,2,3)

del t1[0] #TypeError: 'tuple' object doesn't support item deletion

del t1
print(t1) #NameError: name 't1' is not defined

#loop through a tuple
mytuple = (1,2,3,4)
for i in mytuple:
    print(i)

#tuple methods

a = (1,2,3)
result = a.count(1)
print(result)
result = a.index(2)
print(result)

#tuple operations
t5 = (1,2,3)
print(2 in t5) #True
print(2 not in t5) #False
