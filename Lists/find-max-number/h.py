arr=[]
n=int(input())
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(n):
        if arr[j]<arr[i] and j>i:
            c=arr[j]
            arr[j]=arr[i]
            arr[i]=c
print(arr)
bg=arr[len(arr)-1]
print('this is the biggest number of the list ',(bg))
