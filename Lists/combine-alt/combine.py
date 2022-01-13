n1=int(input())
l1=[]
for i in range(n1):
    f=int(input())
    l1.append(f)

n2=int(input())
l2=[]
for i in range(n2):
    f=int(input())
    l2.append(f)

l3=[]
n_min = min(n1, n2)

for i in range(n_min):
    l3.append(l1[i])
    l3.append(l2[i])

if n1>n2:
    for i in range(n2, n1):
        l3.append(l1[i])
elif n2>n1:
    for i in range(n1, n2):
        l3.append(l2[i])

print(l3)
