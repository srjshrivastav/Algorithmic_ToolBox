import random


def partition3(a, l, r):
    x = a[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            k += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
    a[l], a[j] = a[j], a[l]
    return j, k


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)


n = int(input())
a = list(map(int, input().split()))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')