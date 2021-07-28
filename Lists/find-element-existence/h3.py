n=int(input())
arr=[]
k=int(input())
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(n):
        if arr[j]<arr[i] and j>i:
            c=arr[j]
            arr[j]=arr[i]
            arr[i]=c
print(arr)
for i in arr:
    if i==k:
        print('k is an arr ')
    else:
        print('k is not in arr')