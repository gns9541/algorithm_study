def solution(rows, columns, queries):
    arr = [[0]*(columns+1) for _ in range(rows+1)] # 1,1이 처음 숫자니까 0 으로 패딩
    n=1
    for i in range(1,rows+1):
        for j in range(1,columns+1): # 배열에 숫자 넣어주
            arr[i][j] = n
            n+=1
    
    answer = []
    if len(queries) == 1:  # 범위가 하나면 처음숫자가 답
        answer.append(arr[queries[0][0]][queries[0][1]])
    else:
        for q in queries:
            arr2 = [[0]*(columns+1) for _ in range(rows+1)] # 돌아간거 표시해줄 새로운 배열 생성
            x1=q[0] #2 세로
            y1=q[1] #2 가로
            x2=q[2] #5
            y2=q[3] #4

            di = [0,1,0,-1] #시계방향 우 하 좌 상
            dj = [1,0,-1,0]

            i=x1
            j=y1
            k = 0
            while True: # 돌려
                if k == 4:
                    break
                ni, nj = i+di[k], j+dj[k] # 범위 선에 걸쳐 있는 숫자들만 골라서
                if (j==y1 or i==x1) or (j==y2 or i==x1) or (j==y1 or i==x2) or (j==y2 or i==x2):
                    if y1<=nj<y2+1 and x1<=ni<x2+1: 
                        arr2[ni][nj] = arr[i][j] # 돌려주고
                        i,j = ni,nj # 위치 갱신
                    else:
                        k+=1 # 범위 아니면 방향 전환

            # print(*arr2,sep="\n")
            # print()
            fin = 100000
            for i in range(1,rows+1):
                for j in range(1,columns+1):
                    if arr2[i][j] != 0: # 돌아간 수 중 최솟값 찾기
                        if arr2[i][j]<fin:
                            fin = arr2[i][j]
                        arr[i][j] = arr2[i][j] # 돌아간 배열을 원래 배열에 넣어주고 다음 범위도 돌리기
            # print(*arr,sep="\n") 
            # print()
            answer.append(fin) # 최솟값들
    return answer