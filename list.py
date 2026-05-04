#1 finding the sum,avg, max,min
"""l=[13,29,23,54,50]
sum=0
avg=0
for i in l:
    sum=sum+i
    avg=sum//5
print(sum)
print(avg)
print(max(l))
print(min(l))"""

#2 Reverse a list 
"""l=[13,29,23,54,50]
j=(l[::-1])
print(j)"""

#3 swap element 
"""l=[13,29,23,54,50]
l[0],l[-1]=l[-1],l[0]
print(l)"""

#4 check the name exixt or not 
"""friends=["Iman","Abhinash","Ahana","Lisa","Depandu"]
name=input("Enter your name: ")
if name in friends:
    print(f"Name is in the list: {name}",)
else:
    print(f"Name is not in the list: {name}")"""

#5 check if the list is empty or have element
"""l=[1,2]
if not l:
    print("list is empty")
else:
    print("list is not empty")"""

#6 removing duplicate
"""l=[13,29,23,54,50,13,29]
new=list(set(l))
print(f"old list: {l}, New list: {new}")"""

#7 new list from old list 
"""l=[13,22,23,54,50,14,29]
k=list()
for i in l:
    if i%2==0:
        k.append(i)
print(k)"""

#8 common elements from 2 list
l=[13,22,23,54,50,14,29]
k=[50,23,29,90,44]
g=list(set(l)&set(k))  # way 1 
n=[item for item in l if item in k]  # way 2
print(n)
print(g)








