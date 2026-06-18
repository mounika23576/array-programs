#1smallest element in the array
'''n=int(input())
a=list(map(int,input().split()))
s=a[0]
for i in a:
    if i<s:
        s=i
print(s) '''

#2largest element in the array 
'''n=int(input())
a=list(map(int,input().split()))
s=a[0]
for i in a:
    if i>s:
        s=i
print(s)'''        

#3second smallest element
'''n=int(input())
a=list(map(int,input().split()))
a.sort()
s=a[1]
print(s)'''

# 4second largest element 
'''n=int(input())
a=list(map(int,input().split()))
a.sort()
print(a[-2])'''

#5reverse array
'''n=int(input())
a=list(map(int,input().split()))
print(a[::-1])'''

#6frequency of elements
'''n=int(input())
a=list(map(int,input().split()))
print(a)
d=[]
for i in a:
    if i not in d:
        print(i,a.count(i))
        d.append(i)'''

#7Remove duplicates
'''n=int(input())
a=list(map(int,input().split()))
print(list(set(a)))'''

#8Rotate array by k positions 
'''n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(a[-k:]+a[:-k])'''

#9find the repeated elements 
'''n=int(input())
a=list(map(int,input().split()))
print(a)
a.sort
d=[]
for i in a:
    if i not in d:
        d.append(i)
    else:
        print(i,end=',')''' 

#10find the non repeating elements 
'''n=int(input())
a=list(map(int,input().split()))
print(a)
s=set(a)
d=[]
l=[]
for i in a:
    if i not in d:
        d.append(i)
    else:
        l.append(i)
        s1=set(l)
print(list(s-s1))'''  

#11Equilibrium index 
'''n=int(input())
a=list(map(int,input().split()))
for i in a:
    l=sum(a[i:])
    r=sum(a[:i+1])
    if l==r:
        print(i)
        break'''

#13find the median of the array
'''n=int(input())
a=list(map(int,input().split()))
print(a)
a.sort()
if n%2==0:
    print(a[n//2-1])
else:
    print(a[n//2])''' 

#14array subset check
'''n=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))
print(a)
print(b)
for i in b:
    if i in a:
        print("yes")
        break
    else:
        print("no")'''   

#15search element
'''n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(a)
for i in a:
    if k in a:
        print("found")
        break
    else:
        print("not found")'''

#16missing number
'''n=int(input())
a=list(map(int,input().split()))
print(a)
b=len(a)
for i in range(1,b+1):
    if i not in a:
        print(i)'''
#17leader in array
'''n=int(input())
a=list(map(int,input().split()))
print(a)
for i in range(len(a)):
    if a[i]==max(a[i:]):
        print(a[i],end=' ')'''
#18 union and intersection
'''n=int(input())
a=list(map(int,input().split()))
n1=int(input())
b=list(map(int,input().split()))
print(a)
print(b)
s=set(a)
t=set(b)
print("union",list(s|t))
print("Intersection",list(s&t))'''

#19 Maximum subarray sum
'''n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,len(a)):
    sum=0
    for j in range(i,len(a)):
        sum=sum+a[j]
        s=max(s,sum)
print(s)  '''      
#symmetric pairs
'''n=int(input())
s=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    s.append([a,b]) 
for a,b in s:
    if [b,a] in s:
        print([a,b])          



