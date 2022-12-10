nums = [int(i) for i in input().split()]
max = nums[0]
for i in range (1,len(nums)):
    if nums[i]>max:
        max = nums[i]
print (max)        

