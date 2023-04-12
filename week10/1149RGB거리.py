N = int(input())
cost = [[0,'R','G','B']]+[[0]+list(map(int, input().split())) for _ in range(N)]
print(*cost,sep="\n")
dp = [[0] * (N+1) for _ in range(N+1)]
# for i in range(1,N+1):
#     for j in range(1,N+1):

