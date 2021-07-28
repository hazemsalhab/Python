n=int(input())
a=False
arr=[]
k=int(input())
for i in range(n):
    arr.append(int(input()))
for i in arr:
    if i==k:
        a=True
if a==True:
    print('k is in array')
else:
    print('k is not array')