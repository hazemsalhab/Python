n=int(input())
k=[]
l=[]
for i in range(n):
    f=int(input())
    k.append(f)

for i in range(n-1,-1,-1):
    l.append(k[i])
print(l)
# k.reverse()
# print(l)
# print ("List index-value are : ")
# for i in range(len(k)):
#     print (i, end = " ")
#     print (k[i])