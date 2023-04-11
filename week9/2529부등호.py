from itertools import combinations,permutations
import sys
input = sys.stdin.readline

K = int(input())
S = list(map(str, input().split()))
N = [0,1,2,3,4,5,6,7,8,9]
N1 = [9,8,7,6,5,4,3,2,1,0]


for i in permutations(N1, K + 1):
    i = list(i)
    ans = 0
    for j in range(K):
        if i[j] < i[j + 1] and S[j] == '>':
            pass
        elif i[j] > i[j + 1] and S[j] == '<':
            pass
        else:
            ans+=1
    if ans == K:
        i = "".join(map(str, i))
        print(i)
        break

for i in permutations(N,K+1):
    i = list(i)
    ans = 0
    for j in range(K):
        if i[j] < i[j + 1] and S[j] == '>':
            pass
        elif i[j] > i[j + 1] and S[j] == '<':
            pass
        else:
            ans += 1
    if ans == K:
        i = "".join(map(str, i))
        print(i)
        break



# K = int(input())
# S = list(map(str, input().split()))
# N = [0,1,2,3,4,5,6,7,8,9]
# N1 = [9,8,7,6,5,4,3,2,1,0]
#
#
# for i in permutations(N1, K + 1):
#     i = list(i)
#     ans = 0
#     for j in range(K):
#         if i[j] < i[j + 1] and S[j] == '<':
#             ans += 1
#         elif i[j] > i[j + 1] and S[j] == '>':
#             ans += 1
#     if ans == K:
#         i = "".join(map(str, i))
#         print(i)
#         break
#
# for i in permutations(N,K+1):
#     i = list(i)
#     ans = 0
#     for j in range(K):
#         if i[j]<i[j+1] and S[j] == '<':
#             ans += 1
#         elif i[j]>i[j+1] and S[j] == '>':
#             ans += 1
#     if ans == K:
#         i = "".join(map(str, i))
#         print(i)
#         break