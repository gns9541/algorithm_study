import sys
sys.setrecursionlimit(250000)

def dfs(i,j):
    global ans
    if v[i][j]:
        return v[i][j]
    else:
        v[i][j] = 1
    for k in range(4):
        ni,nj = i+di[k], j+dj[k]
        if 0<=ni<n and 0<=nj<n and tree[ni][nj]>tree[i][j]:
            v[i][j] = max(v[i][j], dfs(ni,nj)+1)
            
    return v[i][j] 
            
    
n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
ans = 0
v = [[0]*n for _ in range(n)]
di = [1,-1,0,0]
dj = [0,0,1,-1]

for i in range(n):
    for j in range(n):
        # v = [[0]*n for _ in range(n)]
        ans = max(dfs(i,j),ans)

print(ans)