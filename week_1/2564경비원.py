garo, sero = map(int, input().split())
s = int(input())
loc =  [list(map(int, input().split())) for _ in range(s)]  # 1:상, 2:하, 3:좌, 4:우
D_dir, D_loc = map(int, input().split())
print(loc)
print(D_dir, D_loc)

di = [0, 1, 0, -1]  # 우 하 좌 상
dj = [1, 0, -1, 0]

lst = [[0]*(garo+1) for _ in range(sero+1)]
for i in range(sero+1):
    for j in range(garo+1):
        for k in range(s):
            if loc[k][0] == 1:
                lst[0][loc[k][1]] = 2
                a = 0
                b = 0
                dr = 0
            elif loc[k][0] == 2:
                lst[sero][loc[k][1]] = 2
                a = sero
                b = garo
                dr = 2
            elif loc[k][0] == 3:
                lst[loc[k][1]][0] = 2
                a = sero
                b = 0
                dr = 3
            elif loc[k][0] == 4:
                lst[loc[k][1]][garo] = 2
                a = 0
                b = garo
                dr = 1

        if i == 0 or i == sero:
            lst[i][j] = 1
        elif j == 0 or j == garo:
            lst[i][j] = 1 

if D_dir == 1:
    lst[0][D_loc] = 3
elif D_dir == 2:
    lst[sero][D_loc] = 3
elif D_dir == 3:
    lst[D_loc][0] = 3
elif D_dir == 4:
    lst[D_loc][garo] = 3    
print(*lst, sep="\n")


cnt = 0
while cnt < (garo*2 + sero*2):
    lst[a][b] == 5
    na, nb = a + di[dr], j + dj[dr]
    if (0 <= na <= sero) and (0 <= nb <= garo) and (lst[na][nb]) != 0:
        a,b = na, nb
    elif lst[na][nb] == 3:
        break
    else: #방향 꺾기
        dr = (dr+1)%4  
        a,b = a + di[dr], b + dj[dr]
    cnt +=1
print(*lst, sep="\n")
print(cnt)
