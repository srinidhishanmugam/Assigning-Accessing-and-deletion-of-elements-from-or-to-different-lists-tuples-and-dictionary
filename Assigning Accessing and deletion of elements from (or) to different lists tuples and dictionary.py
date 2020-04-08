#Assigning elements to different lists
print("List1:")
s1=[1,2,3,4,5]
s1.append('a')
print(s1)
s1.insert(6,2)
print(s1)
s1[6]=4
print(s1)
a="sri"
s1.insert(0,a)
print(s1)
print("List2:")
s2=["we",3,'r']
s2.append(7)
print(s2)
s2.insert(0,1)
print(s2)
s2[2]=4
print(s2)
a="hrm"
s2.insert(4,a)
print(s2)
s2.append(s1)
print(s2)

#Accessing elements from a tuples
t1 = ('physics', 'chemistry', 1997, 2000)
t2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", t1[0])
print ("tup2[1:5]: ", t2[1:5])

#Deleting different dictionary elements
d1={"sri": 30,"madhu": 40,"lavanya":35,"sangu":38}
print(d1)
del d1["sangu"]
print(d1)
a=d1.pop("lavanya")
print(d1)

