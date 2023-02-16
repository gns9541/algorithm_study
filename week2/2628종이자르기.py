g, s = map(int, input().split()) # 가로 세로 길이
N = int(input()) # 칼로 자를 점선의 개수
line = [list(map(int, input().split())) for _ in range(N)]

gl = [[1,0],[1,g]] # 가로로 잘리는 부분 리스트로 (0이랑 g포함) 
sl = [[0,0],[0,s]] # 세로도
for lst in line:
    if lst[0] == 1:
        gl.append(lst)   
        gl.sort()
    elif lst[0] == 0:
        sl.append(lst)
        sl.sort()

sero = []              
garo = []
for i in range(len(gl)-1):       # 위에 잘리는 부분 드러있는 리스트에서 가로 길이 4개 뽑기
    garo.append(gl[i+1][1] - gl[i][1])
for i in range(len(sl)-1):       # 세로도
    sero.append(sl[i+1][1] - sl[i][1])

final = []                   # 뽑은 가로길이 랑 세로길이의 곱에서 가장 큰값 
for i in garo:
    for j in sero:
        final.append(i*j)
print(max(final))




