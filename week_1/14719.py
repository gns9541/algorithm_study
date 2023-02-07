H, W = map(int, input().split())
B = list(map(int, input().split()))
lst = [[0]*W for _ in range(H)] # 블록이 들어갈 수 있는 칸

for i in range(len(B)):
    for j in range(H+1):
        if j == B[i]:
            for idx in range(1, j+1):
                lst[-idx][i] = 1           # 블록 채워지면 1 -> 
# print(*lst, sep='\n') 
# [0, 0, 0, 0, 1, 0, 0, 0]
# [1, 0, 0, 1, 1, 0, 0, 0]
# [1, 0, 1, 1, 1, 0, 0, 1]
# [1, 1, 1, 1, 1, 1, 1, 1]   이런식

cnt_lst = []  
for i in range(H):
    cnt = 0
    for j in range(W):
        if lst[i][j] == 1:
            for jdx in range(1,W-j):
                if lst[i][j+jdx] == 0: 
                    cnt += 1                  # 각 줄의 1이후의 0의 개수 카운트
                elif lst[i][j+jdx] == 1:
                    cnt_lst.append(cnt)       # 다시 1이 나오는 경우에만 카운트를 리스트에 저장
                    break
            cnt = 0                           # 카운트 다시 리셋
print(sum(cnt_lst)) #카운트된 0의 개수의 합 = 고인 빗물의 양

