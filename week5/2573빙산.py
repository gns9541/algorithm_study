# def bfs():
import copy
# 빙산 탐색 함수
# def bfs():
    


N,M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*M for _ in range(N)]

di = [-1, 1, 0, 0] # 상 하 좌 우
dj = [0, 0, -1, 1]

t=0
while True:
    new = copy.deepcopy(arr)
    if t == 2:
        break
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                cnt = 0
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if 0<=ni<N and 0<=nj<M and ice[ni][nj] == 0:
                        cnt += 1
                if ice[i][j] - cnt >= 0:
                    new[i][j] = ice[i][j]
                    new[i][j] = new[i][j] - cnt
                else:
                    new[i][j] = 0
    ice = copy.deepcopy(new)
    t+=1
    print(*new, sep="\n")
    print()

lst = []
for i in range(N):
    for j in range(M):
        if ice[i][j] != 0:
            lst.append([i,j])



visited = [[0]*M for _ in range(N)]
bfs()
