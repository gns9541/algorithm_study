N = int(input())
time = N
bit = [0]*N
lst = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if lst[i][0] == 1:
        bit[i] = lst[i][2]
    
    if bit[i] != 0:
        bit[i] -= 1
    time -= 1
    print(time)
    print(bit)


