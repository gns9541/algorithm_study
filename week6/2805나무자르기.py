N,M = map(int, input().split())
tree = list(map(int, input().split()))
ans = max(tree)

while True:
    take = 0
    for i in range(len(tree)):
        if tree[i]>= ans:
            take += tree[i]-ans
    if take == M:
        break
    ans -= 1
    
print(ans)