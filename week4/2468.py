N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

print(*area, sep="\n")
mx = 0
for lst in area:
    for i in lst:
        if i>=mx:
            mx = i
print(mx)



for k in range(1, mx+1):
    for i in range(N):
        for j in range(N):
            if area[i][j] <= k:
                area[i][j] = 0
    print(*area, sep="\n")
    print()

    
