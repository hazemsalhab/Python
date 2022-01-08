n=int(input())
k=[]
l=[]
for i in range(n):
    f=int(input())
    k.append(f)
for i in range(n-1,-1,-1):
    l.append(k[i])
if (k==l):
    print('yes')
else:
    print('no')
# l=[1,2,3,5,8,4]
# l.sort()
# print(l)
