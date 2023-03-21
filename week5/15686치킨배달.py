import itertools

N,M = map(int, input().split())
city = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]

hlst = []
for i in range(N+1):
    for j in range(N+1):
        if city[i][j] == 1:
            hlst.append([i,j])
# print('가정집',hlst) 가정집 [[1, 4], [2, 1], [2, 3], [4, 4], [4, 5], [5, 4]]

clst = []
for i in range(N+1):
    for j in range(N+1):
        if city[i][j] == 2:
            clst.append([i,j])
# print('치킨집',clst) 치킨집 [[1, 2], [4, 1], [5, 1], [5, 2], [5, 5]]

lst = list(itertools.combinations(clst,M))

ans = []
for i in hlst:
    final = []
    for j in clst:
        final.append(abs(i[0]-j[0])+abs(i[1]-j[1]))
    ans.append(final)  
# print(ans) [[2, 6, 7, 6, 5], [2, 2, 3, 4, 7], [2, 4, 5, 4, 5], [5, 3, 4, 3, 2], [6, 4, 5, 4, 1], [6, 4, 3, 2, 1]]
# 치킨집과 집 사이의 거리들

idx = []
for i in range(len(lst)):
    idx2 = []
    for j in lst[i]:
        if j in clst:
            idx2.append(clst.index(j))
    idx.append(idx2)
# print(idx) [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
# ex) [0,1]이면 위에 ans에서 [2,6],[2,2],[2,4],[5,3],[6,4],[6,4]

fin = []
for i in idx:
    fin2 = []
    for k in ans:
        fin3 = []
        for j in range(len(i)):
            fin3.append(k[i[j]])
        fin2.append(min(fin3))
    fin.append(fin2)   
# 위에 뽑은것들중 최솟값만 뽑아서 리스트에
# print(fin) [[2, 2, 2, 3, 4, 4], [2, 2, 2, 4, 5, 3], [2, 2, 2, 3, 4, 2], [2, 2, 2, 2, 1, 1], [6, 2, 4, 3, 
# 4, 3], [6, 2, 4, 3, 4, 2], [5, 2, 4, 2, 1, 1], [6, 3, 4, 3, 4, 2], [5, 3, 5, 2, 1, 1], [5, 4, 
# 4, 2, 1, 1]]

# 이 중 합이 가장 작은것이 답 
ans = 10000
for lst in fin:
    if ans > sum(lst):
        ans = sum(lst)
print(ans)

        
