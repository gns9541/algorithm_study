N = int(input())
lst_cnt = []
final = []
for N2 in range(1,N+1):
    lst = []
    cnt = 0
    lst.append(N)
    lst.append(N2)
    idx = 0
    while True:
        if lst[idx]-lst[idx+1] >= 0:
            lst.append(lst[idx]-lst[idx+1])
        if lst[idx]-lst[idx+1] < 0:
            break
        idx += 1
    lst_cnt.append(len(lst))
    final.append(lst)
a = max(lst_cnt)
print(a)
for i in final:
    if len(i) == a:
        for j in i:
            print(j, end=" ")
        break