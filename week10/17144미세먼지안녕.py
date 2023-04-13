from copy import deepcopy

R,C,T = map(int, input().split())
arr = [[0]*(C+1)] + [[0]+list(map(int, input().split())) for _ in range(R)]

# 미먼 확산
di = [1,-1,0,0]
dj = [0,0,1,-1]
# 윗공기
dx = [0,-1,0,1] # 우 상 좌 하
dy = [1,0,-1,0]
#아랫공기
da = [0,1,0,-1] # 우 하 좌 상
db = [1,0,-1,0]

t=0
while True:
    if t == T:
        break
    v = [[0]*(C+1) for _ in range(R+1)]
    for i in range(1,R+1):
        for j in range(1,C+1):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt = 0
                for k in range(4):
                    ni,nj = i+di[k],j+dj[k]
                    if 1<=ni<R+1 and 1<=nj<C+1 and arr[ni][nj] != -1:
                        cnt += 1
                        if v[ni][nj] == 0:
                            v[ni][nj] = arr[i][j]//5
                        else:
                            v[ni][nj] += arr[i][j]//5
                v[i][j] += arr[i][j]-(arr[i][j]//5)*cnt

    v1 = [[0]*(C+1) for _ in range(R+1)]
    c = 0
    for x in range(1,R+1):
        if c == 0:
            if arr[x][1] == -1:
                v1[x][1] = -1

                X=x
                k = 0
                y=1
                while True:
                    if k == 4:
                        k = 0
                    nx,ny = x+dx[k], y+dy[k]
                    if 1<=nx<=X and 1<=ny<C+1:
                        if arr[nx][ny] == -1:
                            break
                        v1[nx][ny] = v[x][y]
                        x,y = nx,ny
                    else:
                        k+=1
                c+=1
        if c == 1:
            if arr[x][1] == -1:
                v1[x][1] = -1

                k = 0
                X2=x
                y=1
                while True:
                    if k == 4:
                        k = 0
                    nx,ny = x+da[k], y+db[k]
                    if 1<=nx<R+1 and 1<=ny<C+1:
                        if arr[nx][ny] == -1:
                            break
                        v1[nx][ny] = v[x][y]
                        x,y = nx,ny
                    else:
                        k+=1

    for i in range(2,R):
        for j in range(2,C):
            if i!=X and i!=X+1:
                if v1[i][j] == 0:
                    v1[i][j] = v[i][j] 

    arr = deepcopy(v1)
    t+=1

for i in range(2,R):
    for j in range(2,C):
        if i!=X and i!=X+1:
            if v1[i][j] == 0:
                v1[i][j] = v[i][j] 

ans = 0
for i in range(1,R+1):
    for j in range(1,C+1):
        ans+=v1[i][j]
print(ans+2)








