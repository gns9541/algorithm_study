import copy
# dfs로 돌려주기
def dfs(p, R):
    global ans
    first = copy.deepcopy(R)
    cnt = 0
    if p == num:     # cctv개수만큼 들어갔으면 0개수 세기
        for lst in first:
            cnt += lst.count(0)
        if ans >= cnt:
            ans = cnt
        print(*R, sep="\n")
        print(cnt)
        print()
        return
    i, j, type = cctv[p] # == (2,2,1)
    for k in cctv_watch[type]:
        for l in k: # ex (cctv_watch[type] = [[0],[1],[2],[3]]]
            cctv_see(i,j,l,first)
        dfs(p+1,first)
        first = copy.deepcopy(R)
        
            
N,M = map(int, input().split())
R = [list(map(int, input().split())) for _ in range(N)]

di = [-1,1,0,0] # 상 하 좌 우
dj = [0,0,-1,1]

# cctv 번호 별로 볼 수 있는 방향을 방향벡터의 인덱스로 저장 # 0, 1, 2, 3, 4 
cctv_watch = [[], [[0],[1],[2],[3]], [[0,1],[2,3]], [[0,3],[3,1],[1,2],[2,0]], 
        [[2,0,3],[0,3,1],[3,1,2],[1,2,0]], [[0,1,2,3]]]

cctv = [] 
num = 0
for i in range(N):
    for j in range(M):
        if 1 <= R[i][j] <= 5:
            cctv.append((i,j,(R[i][j])))  
            num += 1 # ex)(2,2,1) 여기서 1 -> 위에 cctv_watch에서 해당하는 번호의 cctv가 볼 수 있는 방향 탐지하기 위해
# print(cctv)

# cctv 보는 곳 찾는 함수
def cctv_see(i,j,k,first):
    l = 1
    while True:
        ni, nj = i + l*di[k], j + l*dj[k]
        if ni<0 or ni>=N or nj<0 or nj>=M or first[ni][nj]==6:
            break 
        if 0<=ni<N and 0<=nj<M:
            if first[ni][nj] == 0:
                first[ni][nj] = '#'
        l+=1
'''
위에 바꾼 #들 다시 초기화하는 함수
def re(i,j,k):
    l = 1
    while True:
        ni, nj = i + l*di[k], j + l*dj[k]
        if ni<0 or ni>=N or nj<0 or nj>=M or R[ni][nj]==6:
            break 
        if 0<=ni<N and 0<=nj<M:
            if R[ni][nj] == '#':
                R[ni][nj] = 0
        l+=1

다시 원래대로 돌려주는 함수 만드니까 돌려줘야 할 부분 넣을 곳 찾기가 어려움
-> decopy 사용해서 초기화 시켜주기
'''


ans = N*M
dfs(0,R)
print(ans)