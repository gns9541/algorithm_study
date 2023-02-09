garo, sero = map(int, input().split())
s = int(input())
loc =  [list(map(int, input().split())) for _ in range(s)]  # 1:상, 2:하, 3:좌, 4:우
D_dir, D_loc = map(int, input().split())

lst = [[0]*(garo+1) for _ in range(sero+1)]

for i in range(sero+1):                                 
    for j in range(garo+1):
        s_lst = []
        for k in range(s):
            if loc[k][0] == 1:
                lst[0][loc[k][1]] = 2
                s_lst.append([0,loc[k][1]])

            elif loc[k][0] == 2:
                lst[sero][loc[k][1]] = 2
                s_lst.append([sero,loc[k][1]])

            elif loc[k][0] == 3:
                lst[loc[k][1]][0] = 2
                s_lst.append([loc[k][1],0])

            elif loc[k][0] == 4:
                lst[loc[k][1]][garo] = 2
                s_lst.append([loc[k][1],garo])        # 길은 1 상점은 2 동근이는 3

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
            
# print(s_lst) 
# print(*lst, sep="\n")

di = [0, 1, 0, -1]  # 우 하 좌 상
dj = [1, 0, -1, 0]

final = 0
for idx in range(len(s_lst)):
    i = s_lst[idx][0]
    j = s_lst[idx][1]
    if i == 0:                # 상점이 동서남북에 어디에 있냐에 따라 시작 방향 다르게 설정
        dr = 0
    elif i == sero:
        dr = 2
    elif j == 0:
        dr = 3
    elif j == garo:
        dr = 1

    cnt = 0                          # 상점에서 시작해서 한칸씩 갈때마다 카운트, 동근이 만나면 멈춤
    while True:   
        ni, nj = i + di[dr], j + dj[dr]
        if (0 <= ni <= sero) and (0 <= nj <= garo) and (lst[ni][nj] != 0):
            i,j = ni, nj
            cnt+=1
            if lst[ni][nj] == 3:
                break
        else: #방향 꺾기
            dr = (dr+1)%4  # 0-1-2-3-0-1-2-...
            
    # print(cnt)
    if cnt > (garo*2 + sero*2)-cnt:     # 카운트랑 전체 둘레 -카운트 비교해서 더 작은 값 합쳐주기
        final += (garo*2 + sero*2)-cnt
    else:
        final += cnt
    # print(final)
print(final)
