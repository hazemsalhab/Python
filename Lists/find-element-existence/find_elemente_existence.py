n=int(input())
f=int(input())
j=False
for i in range(0,n):
    k=int(input())
    if k==f:
        j=True
if j==True:
    print('yes')
else:
    print('no')