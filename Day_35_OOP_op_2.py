"""
# Difference between shallow copy and deep copy
-------------------------------
k = [1,2,3,4]

#shallow copy: same element with different object id
h = k.copy()
print('old:',k,'New:',h)
print('old:',id(k),'New:',id(h))
h.append(100)
print(h,id(h))
print(k)
# Deep copy: same element with same object id
a = k
print('old:',k,'New:',a)

print('old:',id(k),'New:',id(a))

#lets add -1 to k
k.append(-1)
print('k list:',k)
print('a list:',a)
---------------------------------------
# map() function
Higher order function
Syntax: map(func,iter)

it will apply gven function over each element from
iterable

k =[1,2,3,4,5]
#add 100 to each number inside a list
add = lambda num: num+100

print(list(map(add,k)))
-----------------------
n = ['sham','sudha','kishor']

#convert in uppper case
cov = lambda nm:nm.upper()
print(list(map(cov,n)))
===================
k1 = [1,2,3]
k2 = [4,5,6]
lh = []
#elementwise addition
for i in range(len(k1)):
    #print(k1[i]+k2[i])
    lh.append(k1[i]+k2[i])
#print(lh)

print([k1[i]+k2[i] for i in range(len(k1))])
=============================
k = '12345111'
# find() returns lowest index
print(k.find('1'))
# find() returns highest index
print(k.rfind('1'))
-----------------------------
output:
0
7

Process finished with exit code 0
==============================================
# enumerate():

s = 'tanvi desai'
# [('t', 0),('a', 1)...]
e =[]
for i in enumerate(s):
    e.append(i)
print(e)

output:
[(0, 't'), (1, 'a'), (2, 'n'), (3, 'v'), (4, 'i'),
 (5, ' '), (6, 'd'), (7, 'e'), (8, 's'), (9, 'a'), (10, 'i')]

Process finished with exit code 0
========================================================
s= ['male', 'female', 'male', 'female']

# output : [1, 0, 1, 0]

e = []

for i in s:
    if i == 'male'
        e.append(1)
    else:
        e.append(0)
print(e)
--------------------------------------------------
s= ['Male', 'Female', 'Male', 'Female']
# output: [1, 0, 1, 0]
conv = lambda gen:1 if gen=='Male' else 0
print(list(map(conv, s)))

output:

[1, 0, 1, 0]

Process finished with exit code 0
================================================
print(max(10, 20, 30))

output:
30

Process finished with exit code 0
=================================================
for i in range(6): #Rows
    for j in range(6): #Columns
        print('OUT', i, 'IN', j, end=' ')
    print()

output:

OUT 0 IN 0 OUT 0 IN 1 OUT 0 IN 2 OUT 0 IN 3 OUT 0 IN 4 OUT 0 IN 5
OUT 1 IN 0 OUT 1 IN 1 OUT 1 IN 2 OUT 1 IN 3 OUT 1 IN 4 OUT 1 IN 5
OUT 2 IN 0 OUT 2 IN 1 OUT 2 IN 2 OUT 2 IN 3 OUT 2 IN 4 OUT 2 IN 5
OUT 3 IN 0 OUT 3 IN 1 OUT 3 IN 2 OUT 3 IN 3 OUT 3 IN 4 OUT 3 IN 5
OUT 4 IN 0 OUT 4 IN 1 OUT 4 IN 2 OUT 4 IN 3 OUT 4 IN 4 OUT 4 IN 5
OUT 5 IN 0 OUT 5 IN 1 OUT 5 IN 2 OUT 5 IN 3 OUT 5 IN 4 OUT 5 IN 5

Process finished with exit code 0
=====================================================
[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
==> [[10], [20], [30]]

k = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
e = []
for i in k:
    e.append([i[0]])
print(e)


output:
[[10], [40], [70]]

Process finished with exit code 0
==================================================




"""
