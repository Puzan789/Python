a = 'hello'
b = "hello"
c = "Don't worry about apostrophes"
f = '''hello friends wassup
            you people's good
        '''
print(a)
print(b)
print(c)
print(f)


#accessing elements/characters in a string

a = 'hello'
print(a[0])
print(a[4])

#negative indexing
print(a[-1])
print(a[-2])

#slicing a string
print(a[0:2])
print(a[:])

#change items of a string
a[0] = 'H' #TypeError: 'str' object does not support item assignment
print(a)

#delete items of a string
a = 'hello'
del a[0] #TypeError: 'str' object doesn't support item deletion
print(a)

#concatenate strings
a = 'hello'
b = 'world'
c = a + b
print(c)

#iterate through a string
a = 'hello'
for i in a:
    print(i)

#check if string is in a string
s = 'hello'
print('h' in s) #True

#escape sequences/characters
a = 'hello\nworld'
print(a)

b = 'hello\tworld'
print(b)

c = 'hello\\world'
print(c)

#string methods
#format()
a = 'hello'
b = 'world'

print('{} {}'.format(a,b))
print('{1} {0} {1}'.format(a,b))
