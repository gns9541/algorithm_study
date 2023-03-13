from collections import deque

N,M = map(int, input().split())
nums = deque(map(int, input().split()))

# print(nums[3])
i = 0
ans = 0
cnt = 0
while True:
    if len(nums) == 0:
      break
    if ans == M:
        cnt += 1
        nums.popleft()
        i = 0
        ans = 0
    elif i == len(nums):
            nums.popleft()
            i = 0
            ans = 0
    else:
        ans += nums[i]
        i += 1 
print(cnt)
   


    



