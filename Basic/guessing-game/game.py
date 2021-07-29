import random
k= random.randint(1, 100)
gtime=1
while True:
    guess=int(input())
    if guess==k:
        break
    elif guess>k:
        gtime+=1
        print('your guess is bigger than k')
    elif guess<k:
        print('your guess is smaller than k')
        gtime+=1
print('you guessed {} times'.format(gtime))
