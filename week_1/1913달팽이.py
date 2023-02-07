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





