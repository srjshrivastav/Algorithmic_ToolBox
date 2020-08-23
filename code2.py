n = int(input())
if (n <= 1):
    print(n)
else:
    first = 0
    second = 1
    for i in range(2, n + 1):
        nextNum = int(str(first)[-1]) + int(str(second)[-1])
        first = second
        second = nextNum
    print(str(nextNum)[-1])
