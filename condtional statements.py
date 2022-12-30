n=int(input())
res=n%10
print(res)


N=int(input())
y=(N//365)
w=(N%365)//7
d=N-((y*365)+(w*7))
print("No of years:",y)
print("No of weeks:",w)
print("No of day:",d)


#abs diff

list=[10,20,30,40,50]
s=0
for i in range(len(list)):
    s=s+list[i]
print(s)
 #or
list=[10,20,30,40,50]
print(sum(list))

#sum of n natural numbers
n=int(input())
sum=(n*(n+1))/2
print(sum)

n=int(input())
s=0
for i in range(1,n+1):
    s=s+i
print(s)

#product of a given numbers
n=int(input())
p=1
for i in range(1,n+1):
    p=p*i
print(p)

#solid squaree
n=int(input())
for i in range(1,n+1):#col
    for j in range(1,n+1):#row
        print("*",end=" ")
    print(" ")
#solid rectangle
r=int(input())
c=int(input())
for col in range(1,r+1):
    for row in range(1,c+1):
        print("*",end=" ")
    print(" ")

#daigonal
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")



#right angle traingle
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i>=j):
            print("*",end=" ")
    print(" ")

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i<=j):
            print("*",end=" ")
    print(" ")


#reverse diagonal
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j==n+1):
            print("*",end=" ")
        else:
            print(" ", end=" ")
            print(" ")


#equalatoral traingle
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i<=j):
            print("*",end=" ")
        print(" ",end=" ")
    print(" ")


#mirror right angle traingle
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j-i>=0):
            print("*",end=" ")
        print(" ",end=" ")
    print(" ")










