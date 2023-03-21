N,M = map(int, input().split())
r,c,d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)] # 0:청소x 1:벽
visited = [[0]*M for _ in range(N)]

i = r
j = c
di = [-1,0,1,0] # 0:북, 1:동, 2:남, 3:서
dj = [0,1,0,-1]

visited[r][c] = 1
cnt = 1

while True:
    clean = False            
    for _ in range(4):  # 4방향을 돈다 ex) 
        d = (d+3) % 4   # 왼쪽방향으로 한 칸씩 
        ni = i + di[d]  
        nj = j + dj[d]

        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0:  # 범위 안에 들고
            if visited[ni][nj] == 0: # 방문 안했으면
                visited[ni][nj] = 1  # 청소하고
                cnt += 1             # 카운트하고
                i = ni               # 위치를 갱신
                j = nj
                clean = True        # 청소 했다
                break               # for 탈출  # 아니면 위로 올라가 다시 돌기

    if clean == False:               # 다 돌았는데도 청소할 곳이 없다 // 다돌면 처음 바로보는 위치로 돌아감 // 처음이 1이었으면 0 3 2 1 순서
        # 후진 했을 때 벽이면 break
        # 만약 뒤가 벽이 아니라면 위치 갱신
        if room[i-di[d]][j-dj[d]] == 1:  # 위에 i + di[d] 랑 반대되는 개념
            print(cnt)
            break
        else:
            i, j = i-di[d], j-dj[d]

            
print(*visited,sep="\n")