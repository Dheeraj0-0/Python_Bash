nums = [-2,1,-3,4,-1,2,1,-5,4]

cursum = nums[0]
maxsum = nums[0]

for i in range(1,len(nums)):
    cursum = max(nums[i],cursum + nums[i])
    maxsum = max(maxsum,cursum)
print(maxsum)