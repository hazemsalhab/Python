n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
for i in range(n):
    for j in range(i+1,n):
        if arr[j]<arr[i]:
            c=arr[j]
            arr[j]=arr[i]
            arr[i]=c
print(arr)