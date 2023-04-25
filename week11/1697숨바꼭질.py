from collections import deque

N,K = map(int, input().split())
v = [0]*100000
time = 0 


def bfs(i,K):
    q = deque()
    q.append(i)
    v[i] = 1
    t = 0
    while q:
        j = q.popleft()
        if v[j] == 0:
            if v[j+1] == 0:
                
                v[j+1] = 1
                q.append(j+1)
                v[j+1] = 0

            if v[j-1] == 0:
                v[j-1] = 1
                q.append(j-1)
                v[j-1] = 0
            if v[j*2] == 0:
                v[j*2] = 1
                q.append(j*2)
                v[j*2] = 0
        t += 1
        if j == K:
            print(t)
            break
        
bfs(N,K)



