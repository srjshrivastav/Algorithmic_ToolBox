n = int(input())
numbers = []
if (n <= 1):
    print(n)
else:
    numbers.append(0)
    numbers.append(1)
    for i in range(2, n + 1):
        numbers.append(numbers[i - 1] + numbers[i - 2])

    print(numbers[-1])
