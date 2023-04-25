lst = [list(input().split()) for _ in range(5)]
print(lst)
num = []
for i in range(5):
    num.append(int(lst[i][1]))
num.sort()

ref = False
for i in range(4):
    if num[i] != num[i+1]:
        ref = False
        break
    else:
        ref = True
if ref == True:
    ans = 

