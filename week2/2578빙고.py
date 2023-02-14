nums = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
call = sum(call,[])

# print(*nums, sep="\n")
# print(call)

idx = 0    
while idx < 25:
    for i in range(5):
        for j in range(5):
            if call[idx] == nums[i][j]:
                nums[i][j] = 0
    # 가로가 다 0일때
    cnt_garo = 0
    for lst in nums:
        if lst.count(0) == 5:
            cnt_garo += 1
    
    # 전치행렬 -> 세로가 다 0일때
    cnt_sero = 0
    num_rev = list(zip(*nums))
    for lst in num_rev:
        if lst.count(0) == 5:
            cnt_sero += 1
    
    # 대각선 0일때
    sums = []
    sums_rev = []
    cnt_dagak = 0
    for i in range(5):
        for j in range(5):
            if i==j:
                sums.append(nums[i][j])
            elif i+j == 4:
                sums_rev.append(nums[i][j])
    if sum(sums) == 0:
        cnt_dagak += 1
    if sum(sums_rev) == 0:
        cnt_dagak += 1
    
    if (cnt_garo+cnt_sero+cnt_dagak>=3) or (cnt_garo+cnt_sero>=3) or (cnt_sero+cnt_dagak>=3) or (cnt_garo+cnt_dagak>=3) or (cnt_garo >=3) or (cnt_sero >=3):
        print(idx+1)
        break
    # 한번 숫자 넣을때 3보다 커질 수 있는 경우가 있어서 무조건 3보다 '크거나 같을때'로 조건 설정 해줘야함!!!
    idx += 1




    
