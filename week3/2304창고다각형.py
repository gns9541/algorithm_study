N = int(input())
wall = [list(map(int, input().split())) for _ in range(N)]
J = max(wall, key = lambda x : x[0])[0] # 가로길이 최대
I = max(wall, key = lambda x : x[1])[1] # 세로길이 최대
# 가로 가장 큰 위치, 세로 가장 큰 위치 찾아서 배열 만들기

lst = [[0]*(J+1) for _ in range(I+1)]

for p in wall:                           # 배열 중 기둥이 세워져있는 곳에 1 추가해주기
    for j in range(J+1):
        if p[0] == j:
            for i in range(p[1]):       
                lst[i][j] = 1
'''
[0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1]  # 이렇게
[0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1]
[0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1]
[0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1]
[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1]
[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
cnt_lst = []
for i in range(I+1):
    cnt = 0
    for j in range(J+1):
        if lst[i][j] == 1:
            for jdx in range(1,J+1-j):
                if lst[i][j+jdx] == 0: 
                    cnt += 1                  # 각 줄의 1이후의 0의 개수 카운트
                elif lst[i][j+jdx] == 1:
                    cnt_lst.append(cnt)       # 다시 1이 나오는 경우에만 카운트를 리스트에 저장
                    break
            cnt = 0                           # 카운트 다시 리셋
box = 0
for i in wall:
    box += i[1]                # 기둥 넓이까지 더해주기

print(sum(cnt_lst)+box)


