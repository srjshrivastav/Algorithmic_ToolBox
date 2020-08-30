item, cap = list(map(int, input().split()))
given = {}
profit = 0
for i in range(item):
    value, weight = list(map(int, input().split()))
    given[value / weight] = [value, weight]
indProfit = sorted(given.keys(), reverse=True)

for i in indProfit:
    if (given[i][1] <= cap):
        cap -= given[i][1]
        profit += given[i][0]
    else:
        profit += given[i][0] * (cap / given[i][1])
        break
print(profit)
