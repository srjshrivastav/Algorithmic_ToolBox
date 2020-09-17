n = int(input())
arr = sorted(list(map(int, input().split())))
counts = {}


def majel(dic):
    for values in counts.values():
        if (values > n / 2):
            return 1

    return 0


present = False
for i in arr:
    if (i in counts):
        counts[i] = counts[i] + 1
    else:
        counts[i] = 1

print(majel(counts))
