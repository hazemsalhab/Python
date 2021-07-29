n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
k=int(input())
a=0
for i in arr:
    if i==k:
        a+=1
print(a)