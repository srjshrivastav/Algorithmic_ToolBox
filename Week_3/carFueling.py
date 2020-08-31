def canGo(currentStop, nextStop, currentFuel):
    if (nextStop - currentStop <= currentFuel):
        return True
    return False


d = int(input())
atOneFill = int(input())
stations = int(input())
stationD = list(map(int, input().split()))
stationD.insert(0, 0)
stationD.append(d)
i = 0
fills = 0
reached = True
currentFuel = atOneFill
while (i < len(stationD) - 1):
    if (stationD[i + 1] - stationD[i] > atOneFill or currentFuel < 0):
        print(-1)
        reached = False
        break
    elif (not canGo(stationD[i], stationD[i + 1], currentFuel)):
        fills += 1
        currentFuel = atOneFill
    currentFuel -= stationD[i + 1] - stationD[i]
    i += 1
if (reached):
    print(fills)
