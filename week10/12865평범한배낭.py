N, K = map(int, input().split())
lst = [[0,0]]+[list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1):      # i: 물건 종류
    for j in range(1,K+1):  # j: 현재 물건을 담을 수 있는 정도 
        w,v = lst[i]        # w: 물건의 무게, v: 물건의 가치
        if j >= w:          # 물건의 무게가 현재 가방이 담을 수 있는 무게보다 작으면
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]
        # print(i,j)
        print(*dp,sep="\n")
        print()
print(dp[i][K])
print(*dp,sep="\n")


'''
    |1	 2	 3	 4	 5	 6	 7   가능한 무게(j) |  물건 무게(w)
13  |0	 0	 0	 0	 0	 13	 13                |      6
8   |0	 0	 0	 8	 8	 13	 13                |      4
6   |0	 0	 6	 8	 8	 13	 14                |      3
12  |0	 0	 6	 8	 12	 13	 14                |      5  
    |
가치(v) 

<dp>
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 8, 8, 13, 13]
[0, 0, 0, 6, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 12, 13, 14]

'''

