from collections import deque

N = int(input())
# num = list(map(int, input().split()))
num = deque(list(map(int, input().split())))
stack = []
i = 1

while len(num)>=1:
    if i == len(num):
        stack.append(-1)
        # num.pop(0)
        num.popleft()
        i = 1
        
    elif num[i] > num[0]:
        stack.append(num[i])
        # num.pop(0)
        num.popleft()
        i = 1
        
    else:
        i+=1
print(*stack)
    
#네임에러
#이것도 왜 시간초과

# N = int(input())
# num = list(map(int, input().split()))

# for i in range(N):
#     cnt = 0
#     for j in range(N-i):
#         if num[i] < num[i+j]:
#             ans = num[i+j]
#             cnt+=1
#             break
#         elif num[i] > num[i+j]:
#             cnt += 1
#         if cnt == N-i-1:
#             ans = -1
#             break
#     print(ans, end=" ")

