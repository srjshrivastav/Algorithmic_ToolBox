import random


def partition3(a, l, r):
    i = l
    value = a[l]
    while i <= r:
        if a[i] == value:
            i += 1
        elif a[i] < value:
            a[i], a[l] = a[l], a[i]
            i += 1
            l += 1
        else:
            a[i], a[r] = a[r], a[i]
            r -= 1
    return l, r


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