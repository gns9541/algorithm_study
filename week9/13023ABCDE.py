def dfs(n,k):       
    if n==5:            # 다섯번 새로운노드 방문하면 탈출하고
        print(1)        # 1출력
        exit()
    for i in arr[k]:    # 방문한 노드와 ㅇ인접한 노드들 중에서
        if v[i] == 0:   # 방문 안한 노드
            v[i] = 1    # 방문하고 
            dfs(n+1,i)  # 다시 dfs
            v[i] = 0    # 위에 방문한곳 말고 다른 인접 노드도 들어가봐야하니까 원래대로 돌려주기
        

N,M = map(int, input().split())    # 사람 수, 관계 수
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)               # 인접 리스트 만들기 ex) [[1,3], [0,2,4], [1,3], [2,0], [1]]
    arr[b].append(a)                    

ans = 0
v = [0]*N

for k in range(N):    # 시작노드 다르게 정하기
    v[k] = 1          # 시작노드에 방문표시하고
    dfs(1,k)          # dfs 돌리고 (인자는 dfs깊이, 방문 노드)
    v[k] = 0          # 원래대로 돌려줘

print(0)              # 탈출조건 해당 안되면 0 출력
