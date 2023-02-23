# 아 몰라

N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split())) # 0:+ 1:- 2:* 3://
print(A, C)
stack = [0]*(len(A)+N-1)

print(stack)

for i in range(len(stack)):
    if i%2 == 0:
        stack[i] = A[i//2]
    else:
        stack[i] = #
print(stack)

arr = [1, 2, 3]
N = 3
sel = [0] * N # 결과들이 저장될 리스트
check = [0] * N # 해당 원소를 이미 사용했는지 안했는지 체크
def perm(idx):
 # 다 뽑아서 정리
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i] # 값을 써라
                check[i] = 1 # 사용했다는 표시
                perm(idx+1)
                check[i] = 0 # 다음 반복문을 위한 원상복구
perm(0)