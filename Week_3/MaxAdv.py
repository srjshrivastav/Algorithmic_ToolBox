n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
maxAd = 0
for i in range(n):
    maxAd += (a[i] * b[i])
print(maxAd)
