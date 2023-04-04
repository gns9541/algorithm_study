lst = list(map(int, input().split())) #[50 0 0 50]
N = lst.pop(0)
# arr = [[0]*30 for _ in range(30)]
# print(*arr,sep="\n")
di = [0,0,1,-1] # 동 서 남 북
dj = [1,-1,0,0]
ans = 0
fin = 0
def dfs(i,j,cnt,ans,k):
    global fin
    ni,nj = i+di[k],j+dj[k]
    if v[i][j] == 1:
        return
    
    if cnt == N:
        fin += ans
        # print(ans)
        # print(*v,sep="\n")
        return
    
    if v[i][j] == 0:
        v[i][j] = 1
        for p in range(4):
            dfs(ni,nj,cnt+1,ans*lst[k]/100,p)
        v[i][j] = 0
        

v = [[0]*30 for _ in range(30)]
for k in range(4):
    if lst[k] != 0:
        dfs(15,15,0,1,k)
print(fin/4)