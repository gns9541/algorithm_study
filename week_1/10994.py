# N = int(input())
# for i in range(1, N+1):
    
#     print("*"+"*"*4*(N-1))

# # print("*"+*4*((N-1)-1)+"*")

# N = int(input())

def star(N):
    # N = int(input())
    if N > 100:
        return
    star(N)
    print("*"+"*"*4*(N-1))
    return


star(int(input()))

    