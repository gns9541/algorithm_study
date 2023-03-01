N = int(input())
all_dice = []
# 주사위 전개도에서 마주보는 짝대로 묶어서 리스트 만들기 [[A,F],[B,D],[C,E]]
for _ in range(N): 
    dice = list(map(int,input().split()))
    d1 = [] # A, F
    d2 = [] # B, D
    d3 = [] # C, E
    d1.append(dice[0])
    d1.append(dice[5])
    d2.append(dice[1])
    d2.append(dice[3])
    d3.append(dice[2])
    d3.append(dice[4])
    df = [d1,d2,d3]
    all_dice.append(df)
# print(*all_dice, sep="\n")           

# 주사위를 쌓을 수 있는 모든 경우의 수
stack = []
for j in range(3): # 첫번째 주사위는 어떤 방향으로든 둘 수 있음 -> 경우의 수 6개
    i = 0
    stack1 = [] # A, B, C를 바닥으로 시작하는 경우
    stack2 = [] # F, D, E를 바닥으로 시작하는 경우
    while True:       
        if i == N: # 주사위 개수만큼 쌓으면 탈출
            break
        if stack1: # 스택이 차있으면 
            for k in range(3): # 스택 마지막 인덱스의 값과 같은 부분 푸쉬하고 그 맞은편도 같이 푸쉬 해주기 
                for l in range(2):
                    if stack1[-1] == all_dice[i][k][l]:
                        stack1.append(all_dice[i][k][l])
                        if l == 0:
                            stack1.append(all_dice[i][k][1])
                        else:
                            stack1.append(all_dice[i][k][0])
                        break
        if stack2:
            for k in range(3):
                for l in range(2):
                    if stack2[-1] == all_dice[i][k][l]:
                        stack2.append(all_dice[i][k][l])
                        if l == 0:
                            stack2.append(all_dice[i][k][1])
                        else:
                            stack2.append(all_dice[i][k][0])
                        break
        
        if len(stack1) == 0 or len(stack2) == 0: # 스택이 없으면 위 아래 뒤집어 둘다 푸쉬 해주기
            stack1.append(all_dice[i][j][0])
            stack1.append(all_dice[i][j][1])
            stack2.append(all_dice[i][j][1])
            stack2.append(all_dice[i][j][0])
            
        i += 1 # 위 조건 모두 돌았으면 다음 주사위로 넘어가
    # 6가지 경우 한곳에
    stack.append(stack1) 
    stack.append(stack2)
    
# print(*stack,sep="\n")
# 쌓아진 주사위의 위 아래 면을 제외한 부분에서 가장 큰값들 끼리 모두 더해
ans = 0
for lst in stack:
    sum = 0
    for i in range(0, 2*N, 2):
        num = [1,2,3,4,5,6]
        num.remove(lst[i])
        num.remove(lst[i+1])
        # print(num)
        sum += (max(num))
    if ans <= sum: # 그 중 가장 큰 값이 정답
        ans = sum
        
print(ans)
    
