#lis=['iman','arafat','jon']
#for i in lis:
#    print(i)

#tup=('iman','arafat','jon')
#for j in lis:
#    print(j)
    

#s="iman"
#for k in lis:
#    print(k)

## patterns

#for i in range(5,-1):
#    for j in range(i):
#        print("*", *i)
#    print() 

# fibonacci series 
last=int(input("Enter the range: "))
first=0
second=1
for i in range(0,last):
    print(first, end=" ")
    fibo=first+second
    first=second
    second=fibo
        