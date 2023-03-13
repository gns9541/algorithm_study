N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
lst = []
for i in range(N):
    lst.append(i)


final = [0]*N


for i in range(N):
    final[P[i]] = i
print(final)

card = [0]*N
cnt = 0
# while True:
#     if cnt == 0:
#         for i in range(len(card)):
#             card[S[lst[i]]] = lst[i]

#     else:
#         for i in range(len(card)):
#             card[S[card[i]]] = card[i]
#     print(card)
#     cnt += 1
#     if card == final:
#         break
for i in range(N):
     card[S[lst[i]]] = lst[i]
lst = card
print(lst)
for i in range(N):
     card[S[lst[i]]] = lst[i]
print(card)
print(lst)


