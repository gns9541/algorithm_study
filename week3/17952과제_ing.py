N = int(input())
stk = []
final = 0
# lst = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
for _ in range(N):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        if lst[2] == 1:
            final += lst[1]
        else:
            stk.append([lst[1], lst[2]-1])
    # print(stk)
    if stk:
        stk[-1][1] -=1
        if stk[-1][1] == 0:
            final += stk.pop()[0]
    # print(stk)
print(final)
# 시간초과


