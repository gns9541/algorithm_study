from collections import deque
import sys
input = sys.stdin.readline
MAX = sys.maxsize

di = [1,-1,0,0]
dj = [0,0,1,-1]
def bfs():
    q = deque([(0,0)])
    v = [[MAX]*N for _ in range(N)]
    v[0][0] = arr[0][0]
    
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni,nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # if v[ni][nj] == 0:
                #     v[ni][nj] = v[i][j] + arr[ni][nj]
                #     q.append([ni,nj])
                # elif v[ni][nj] > 0:
                if v[ni][nj] > v[i][j]+arr[ni][nj]:
                    v[ni][nj] = v[i][j]+arr[ni][nj]
                    q.append([ni,nj])
    return v[N-1][N-1]


n = 0
while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    n+=1
    print(f"Problem {n}:", bfs())
    
