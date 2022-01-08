n=int(input())
f=0
for i in range(1,n+1):
    guess_number=int(input())
    if guess_number>f:
        f=guess_number
print(f)