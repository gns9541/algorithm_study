def pre(i):
    if i:
        ans1.append(idx[i])
        pre(idx.index(c1[i]))
        pre(idx.index(c2[i]))

def inorder(j):
    if j:
        inorder(idx.index(c1[j]))
        ans2.append(idx[j])
        inorder(idx.index(c2[j]))

def post(i):
    if i:
        post(idx.index(c1[i]))
        post(idx.index(c2[i]))
        ans3.append(idx[i])


N = int(input())
alpha = [list(map(str, input().split())) for _ in range(N)]

c1 = [0]*(N+1)
c2 = [0]*(N+1)
idx = ['.']
for i in alpha:
    idx.append(i[0])

# print(*alpha, sep="\n")
for i in range(1,len(alpha)+1):
    if c1[i] == 0:
        c1[i] = alpha[i-1][1]
    if c1[i] != 0:
        c2[i] = alpha[i-1][2]

ans1 = []
ans2 = []
ans3 = []
pre(1)
inorder(1)
post(1)
ans1 = "".join(ans1)
ans2 = "".join(ans2)
ans3 = "".join(ans3)
print(ans1)
print(ans2)
print(ans3)