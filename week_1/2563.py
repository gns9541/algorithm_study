N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]
# print(p)

x = []
y = []
for i in range(0, 100):
    x.append(i)
    y.append(i)

paper = []
for i in range(100):
    for j in range(100):
        paper.append((x[i],y[j]))
# print(paper)
cnt = 0
for j in range(len(p)):
    
    x1=[]
    y1=[]
    for i in range(0, 10):
        x1.append(p[j][0]+i)
        y1.append(p[j][1]+i)

    # print(x1,y1)
    pf = []
    for i in (x1):
        for jdx in y1:
            pf.append((i,jdx))
    # print(pf)

    # cnt = 0
    for idx in pf:
        if idx in paper:
            paper.remove(idx)
            cnt += 1
        elif idx not in paper:
            pass
        
print(cnt)
    






















# x = []
# y = []
# for i in range(0, 100):
#     x.append(i)
#     y.append(i)

# paper = []
# for i in range(10):
#     for j in range(10):
#         paper.append((x[i],y[j]))
# # print(paper)

# # (3,7) -> (13,7), (3, 17), (13, 17)
# cnt = 0
# for i in range(len(p)):
#     for (a, b) in paper:
#         if b == p[i][1] and a == p[i][0]:
#             for j in range(0,11):
#                 cnt += 1
        
# print(paper)
# cnt = 0
# for idx in range(N):
#     for i in x:
#         for j in y:
#             if p[idx][0] == i and p[idx][1] == j:
                
#                 cnt += 1
#     print(cnt)


