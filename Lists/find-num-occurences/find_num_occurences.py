n=int(input())
j=0
s=[]
for i in range(0,n):
    n_numbers=int(input())
    s.append(n_numbers)
k=int(input())
for l in s:
    if k==l:
        j+=1
print(j)