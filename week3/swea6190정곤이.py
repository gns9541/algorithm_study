T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))

    lst = []
    for i in num:
        for j in num:
            if i!=j and i*j not in lst:
                lst.append(i*j)
    # print(lst)

    lst = list(map(str, lst))
    # print(lst)
    for i in range(len(lst)):
        ans = 1
        for j in range(len(lst[i])-1):
            if lst[i][j] > lst[i][j+1]:
                ans = 0
                lst[i] = 0
    
    lst = list(map(int, lst))
    if sum(lst) == 0:
        ans = -1
    else:
        ans = max(lst)
    print(f"#{test_case} {ans}")
    ### 런타임 에러ㅗ