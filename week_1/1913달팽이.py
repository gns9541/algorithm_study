di = [1, 0, -1, 0]  # 하 우 상 좌 
dj = [0, 1, 0, -1]

N = int(input())
lst = [[0]*N for _ in range(N)]
P = int(input())

i = 0   # 0,0 부터 시작해서 시계 반대 방향으로 말기
j = 0   
dr = 0
  
for cnt in range(N*N, 0, -1):
    lst[i][j] = cnt             #  좌표에 숫자 내림차순으로 기록
    ni,nj = i+di[dr], j+dj[dr]   
 
        
    if 0<=ni<N and 0<=nj<N and lst[ni][nj]==0:  # 다음 위치가 범위내 아니면 0인경우 이동
        i,j = ni,nj
    else:                                         # 방향을 꺾고 이동위치 다시 
        dr = (dr+1)%4                             # 하 우 상 좌 순으로
        i,j = i+di[dr], j+dj[dr]
 
for i in lst:
    print(*i)

for i in range(N):
    for j in range(N):
        if lst[i][j] == P:
            print(i+1, j+1)

###############################################################################
# 알고리즘 배우기 전 노가다,,

N = int(input())
lst = [[0]*N for _ in range(N)]
P = int(input())

# print(*lst, sep='\n')
# print(lst)

lst_num = []
for i in range(1, N**2+1):
    lst_num.append(i)

# print(lst)
a = int((N-1)/2)
b = int((N-1)/2)
lst[a][b] = 1
way = "U"
num = 1
cnt = 1

while num < N**2:
    # num = 2
    if way == "U": #위
        for i in range(cnt):
            num += 1
            a -= 1
            lst[a][b] = num

            if num == N**2:
                break
        way = "R"

    elif way == "R": #오른쪽
        for i in range(cnt):
            num += 1
            b += 1
            lst[a][b] = num
        way = "D"
        cnt += 1

    elif way == "D": #아래
        for i in range(cnt):
            num += 1
            a += 1
            lst[a][b] = num
        way = "L"
    
    elif way == "L": #왼쪽
        for i in range(cnt):

            num += 1
            b -= 1
            lst[a][b] = num
        way = "U"
        cnt += 1
    
for i in lst:
    print(*i)
for i in range(N):
    for j in range(N):
        if lst[i][j] == P:
            print(i+1, j+1)

