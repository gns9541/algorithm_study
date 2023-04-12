N, K = map(int, input().split())
lst = [[0,0]]+[list(map(int, input().split())) for _ in range(N)]
# print(lst)
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1):      # i: 물건 종류
    for j in range(1,K+1):  # j: 현재 물건을 담을 수 있는 정도 
        w,v = lst[i]      # w: 물건의 무게, v: 물건의 가치
        if j >= w:          # 물건의 무게가 현재 가방이 담을 수 있는 무게보다 작으면
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]
        # print(i,j)
        # print(*DP,sep="\n")
        # print()
print(dp[i][K])





# import sys
# input = sys.stdin.readline

# def dfs(w,res):
#     global ans
#     if w==K:
#         ans = max(ans, res)
#         return

#     for j in range(N):
#         if v[j] == 0:
#             if w+lst[j][0]>K:
#                 ans = max(ans, res)
#                 pass
#             else:
#                 v[j] = 1
#                 dfs(w+lst[j][0],res+lst[j][1])
#                 v[j] = 0



# N,K = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(N)]
# v = [0]*N
# ans = 0
# for i in range(N):
#     v[i]=1
#     dfs(lst[i][0],lst[i][1])
#     v[i]=0
# print(ans)
    

