g, s = map(int, input().split()) # 가로 세로 길이
N = int(input()) # 칼로 자를 점선의 개수
line = [list(map(int, input().split())) for _ in range(N)]

gl = [[1,0],[1,g]]
sl = [[0,0],[0,s]]
for lst in line:
    if lst[0] == 1:
        gl.append(lst)
        gl.sort()
    elif lst[0] == 0:
        sl.append(lst)
        sl.sort()

sero = []
garo = []
for i in range(len(gl)-1):
    garo.append(gl[i+1][1] - gl[i][1])
for i in range(len(sl)-1):
    sero.append(sl[i+1][1] - sl[i][1])

final = []
for i in garo:
    for j in sero:
        final.append(i*j)
print(max(final))




