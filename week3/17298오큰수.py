N = int(input())
num = list(map(int, input().split()))
for i in range(N):
    cnt = 0
    for j in range(N-i):
        if num[i] < num[i+j]:
            ans = num[i+j]
            cnt+=1
            break
        elif num[i] > num[i+j]:
            cnt += 1
        if cnt == N-i-1:
            ans = -1
            break
    print(ans, end=" ")
