
for _ in range(4):
    nums = list(map(int,input().split()))
    ans = 'a'

    # ((0 1) (2 3)) ((4 5) (6 7))  
    if nums[2] < nums[4] or nums[6] < nums[0] or nums[1] > nums[7] or nums[3] < nums[5]:
        ans = 'd'
    elif nums[0]==nums[6] or nums[4]==nums[2]:
        if nums[3]==nums[5] or nums[7]==nums[1]:
            ans = 'c'  
        else:
            ans = 'b'        
    elif nums[3]==nums[5] or nums[7]==nums[1]:
            ans = 'b'
            
    print(ans)
        


    
    