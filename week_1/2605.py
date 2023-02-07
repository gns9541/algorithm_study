N = int(input())
S = list(map(int, input().split()))
lst = []
i = 0

for j in S:
    lst.insert(j,i+1)
    i += 1

lst.reverse()

for i in lst:
    print(i, end=" ")



