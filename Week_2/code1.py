n = int(input())
if (n <= 1):
    print(n)
else:
    first = 0
    second = 1
    for i in range(2, n + 1):
        nextNum = first + second
        first = second
        second = nextNum

    print(nextNum)
