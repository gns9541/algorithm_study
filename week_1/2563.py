N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]

x = []
y = []
for i in range(0, 100):
    x.append(i)
    y.append(i)

paper = []
for i in range(100):
    for j in range(100):
        paper.append((x[i],y[j]))        # 100칸짜리 도화지에 좌표찍음
# print(paper)
cnt = 0
for j in range(len(p)):
    
    x1=[]
    y1=[]
    for i in range(0, 10):               # 색종이의 좌표 
        x1.append(p[j][0]+i)
        y1.append(p[j][1]+i)

    pf = []
    for i in (x1):                  
        for jdx in y1:
            pf.append((i,jdx))            # 색종이 좌표를 찍음

    for idx in pf:
        if idx in paper:
            paper.remove(idx)
            cnt += 1                      # 도화지에 색종이 좌표 있음 빼버리기고 그만큼 수 세기
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


