from collections import deque

def dfs(i,j):
    global cnt
    if arr[i][j] == 1:   # 3-1. (i,j)가 1이면 cnt하나 올려주고
        cnt += 1        
        arr[i][j] = 0    # 3-2. 그 배열 0으로 바꿔주기
        for k in range(4):  
            ni, nj = i+di[k],j+dj[k]   # 3-3 .그리고 동서남북 방향으로 한칸씩 보면서 범위조건 안에 들어가고 1이면 
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1: 
                dfs(ni,nj) # 3-4. dfs 다시 들어가기
 


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

di = [1,-1,0,0]  # 방향 정해주기
dj = [0,0,1,-1]
ans = []
ans2 = 0
for i in range(N):           # 1. (0,0)부터 배열 돌면서
    for j in range(N):       
        if arr[i][j] == 1:   # 2. 배열에 1이 있으면 단지내 집 개수 cnt = 0 으로 정의
            cnt = 0                
            dfs(i,j)         # 3. dfs돌기
            ans.append(cnt)  # 4. 더이상 인접한 1이 없으면 1개수 센거 ans에 추가해주고
            ans2+=1          # 5. 단지 수 하나 올려주고 다음 배열로

# 6. 위 dfs함수에서 단지 안 인접한 1들은 모두 0으로 처리해 줬기 때문에 dfs를 빠져나온후 다음 배열로을 돌면서 찾은 1은 다음 단지일 수밖에 없다.
            
print(ans2)
ans.sort()
for i in ans:
    print(i)  # 7. 마지막으로 단지 수 와 단지 내 집의 수를 오름차순으로 정렬 후 출력
