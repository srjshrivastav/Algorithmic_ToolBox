nel = list(map(int, input().split()))
n = nel[0]
el = nel[1:]
Kkel = list(map(int, input().split()))
K = Kkel[0]
Kel = Kkel[1:]


def search(els, low, high, Key):
    if (high >= low):
        mid = (high + low) // 2

        if (els[mid] == Key):
            return mid
        elif (els[mid] < Key):
            return search(els, mid + 1, high, Key)
        else:
            return search(els, low, mid - 1, Key)
    else:
        return -1


for i in Kel:
    print(search(el, 0, n - 1, i), end=" ")
print()
