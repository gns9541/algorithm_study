# def f(i):
#     if node[i] != []:
#         print(i)
#         v.append(i)
#         f(node[i][0])
#         node[i].pop(0)
#     else:
#         return


# N, M = map(int, input().split())
# lst = [list(map(int,input().split())) for _ in range(M)]

# print(*lst)
# node = [[] for _ in range(N+1)]
# print(node)
# for i in lst:
#     node[i[0]].append(i[1])
# print(node)
# v = []
# f(1)

def DFS(x):
    visited[x] = 1

    for i in arr[x]:
        if visited[i] == 0:
            DFS(i)

N, M = map(int, input().split())
# 인접 리스트 
arr = list([] for _ in range(N+1))
cnt = 0
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, N+1):
    if visited[i] == 0:
        DFS(i)
        cnt += 1

print(cnt)