# n: 행번호
# N행으로 진행 -> 성공 시 ans +=1
# 0행부터 Q놓고 그 다음행으로 -> 트리 만들기 .... N행에 도달하면 종료, 성공했으니 ans+=1
    # v -> 열 라인 체크 visited 배열로 Q놓고 갈수있는 해당 열(세로) check 해주기 ex) v1[j] = 1
    # v1 -> 대각선 1 체크  대각선은 Q가 놓인 위치인 i+j에 표시 ex) v2[i+j] = 1
    # v2 -> 대각선 2 체크  대각선은 Q가 놓인 위치인 i-j에 표시 ex) v2[i-j] = 1

def dfs(n):
    global ans
    if n == N: # 종료조건
        ans += 1
        return
    # 하부함수 호출
    for j in range(N):
        if v[j]==v1[n+j]==v2[n-j]==0:
                # visited 표시
                v[j]=v1[n+j]=v2[n-j] = 1
                dfs(n+1)
                # visited 표시헤제
                v[j]=v1[n+j]=v2[n-j] = 0


N = int(input())
ans = 0
v = [0]*N
v1 = [0]*(2*N)
v2 = [0]*(2*N)
dfs(0)
print(ans)
