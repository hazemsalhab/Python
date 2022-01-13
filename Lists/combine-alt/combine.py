n1=int(input())
t=0
s=0
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

if n1>n2:
    for i in range(n2*2):
        if (i%2)==0:
            l3.append(l1[t])
            t+=1    
        else:
            l3.append(l2[s])
            s+=1 
    for i in range(n1-1,n2-1,-1):
        l3.append(l1[i])
elif n2>n1:
    for i in range(n1*2):
        if (i%2)==0:
            l3.append(l1[t])
            t+=1    
        else:
            l3.append(l2[s])
            s+=1
    for i in range(n2-1,n1-1,-1):
        l3.append(l2[i])
elif n2==n1:
    for i in range(n1+n2):
        if (i%2)==0:
            l3.append(l1[t])
            t+=1    
        else:
            l3.append(l2[s])
            s+=1  
print(l3)
