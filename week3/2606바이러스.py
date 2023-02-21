def dfs_stk(start):
    v = [0] * (V + 1)
    stk = []

    s = start
    v[s] = 1
    alst.append(s)

    while True:
        for e in range(1, V + 1):
            if v[e] == 0 and adj[s][e]:
                stk.append(s)  # 되돌아올 위치

                s = e
                v[s] = 1
                alst.append(s)
                break  
        else:  #  연결된 방문노드 없는 경우 
            if stk:
                s = stk.pop()  # 기준
            else:
                break  # 탐색할 기준점 없음


V = int(input()) 
E = int(input())
# 연결행렬에 
adj = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    s, e = map(int, input().split())
    adj[s][e] = adj[e][s] = 1

# print(*adj, sep="\n")
alst = []
dfs_stk(1)
print(len(alst)-1)