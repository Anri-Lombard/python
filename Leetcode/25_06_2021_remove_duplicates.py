def removeDuplicates(nums):
    for idx, num in enumerate(nums):
        if nums.count(num) > 1:
            nums = [nums.replace(num, "_")]
            nums[idx] = num
        print(nums)
        
        
removeDuplicates([1,1,2,323])