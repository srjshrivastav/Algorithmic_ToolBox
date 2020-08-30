n = int(input())
coins = 0
while (n):
    if (n - 10 >= 0):
        n -= 10
        coins += 1
        continue
    elif (n - 5 >= 0):
        n -= 5
        coins += 1
        continue
    else:
        n -= 1
        coins += 1
print(coins)
