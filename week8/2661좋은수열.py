def check(lst):
    for i in range(1, len(lst)//2+1):
        if lst[-i:] == lst[-(i*2):-i]:
                return False
    return True

def dfs(n):
    global ans
    if not check(n):
        return
    if len(n) == N:
        ans = min(ans, int(n))
        print(ans)
        exit(0)
        
    for j in range(3):
        if num[j] != n[-1]:
            dfs(n+num[j])
    

N = int(input())
num = ['1','2','3']
ans = 10**(N)

dfs(num[0])