#creating a set
a = {1,2,3,3,4,5,5}
b = {4,'five',6}
c = {'seven',8,9.0}

l = [1,2,3,3,4,5,5]
s = set(l)
print(s)

s1 = set() #creating an empty set


#add, update set
s1.add(1)
s1.add(2)
s1.add(3)
print(s1)

s1.update([4,5,6])
print(s1)

#removing elements from a set

s1.remove(1)
print(s1)

s1.discard(2)
print(s1)

s1.pop()
print(s1)
s1.clear()
print(s1)

#iterate through a set

s2 = {1,2,3,4,5,6}
for i in s2:
    print(i)

# check if an element is in a set
s2 = {1,2,3,4,5,6}
print(1 in s2) #True
print(7 in s2) #False
