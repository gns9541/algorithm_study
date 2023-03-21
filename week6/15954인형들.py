N,K = map(int, input().split()) # N종류의 인형, 
P = list(map(int, input().split()))
lst = []
while True:
    if K==N+1:
        break
    for i in range(len(P)-K+1):
        add = 0
        for j in range(i,i+K):
            add+=P[j]
        # print(add)
        m = add/K   
        add = 0
        for j in range(i,i+K): 
            add += (P[j]-m)**2
        b = add/K
        p = abs(b**(1/2))
        lst.append(p)
    K+=1
# print(lst)
print(min(lst))

### python3은 시간초과 pypy3은 되네