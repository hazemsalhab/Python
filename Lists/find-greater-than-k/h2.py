arr=[]
n=int(input())
for i in range(n):
    arr.append(int(input()))
k=int(input())
ar=[]
for i in range(n):
    if arr[i]>k:
        ar.append(arr[i])
print(ar)

