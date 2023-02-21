T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    print(farm)
    
    add = 0
    for i in range(N):
        if i < N//2:
            for k in range(i+1):
                add += farm[i][N//2+k]
                add += farm[i][N//2-k]
            add -= farm[i][N//2]
        elif i > N//2:
            for q in range(N-i):
                add += farm[i][N//2+q]
                add += farm[i][N//2-q]
            add -= farm[i][N//2]
        
    final = add + sum(farm[N//2])
    print(f"#{test_case} {final}")

