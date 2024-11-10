from random import randrange
r = randrange(1,101)
u = int(input())
while u != r:
    print("Вы не угадали")
    u = int(input())
print("Вы угадали")