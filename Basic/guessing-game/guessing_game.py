import random
n = random.randint(1, 1000)
n_tries =0
while True:
    guess=int(input())
    n_tries+=1
    if guess==n:
        print(n_tries)
        break
    elif guess>n:
        print('high')
    elif guess<n:
        print('low')