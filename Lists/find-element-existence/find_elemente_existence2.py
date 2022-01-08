n=int(input())
f=int(input())
j=False
s=[]
for i in range(0,n):
    k=int(input())
    s.append(k)
for l in s:
    if l==f:
        j=True
if f in s or j==True:
    print('yes')
else:
    print('nop')
