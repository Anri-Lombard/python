class Solution:
    def largestSumAfterKNegations(self, nums, k):
        while k > 0:
            index = 0
            lowest_num = max(nums)
            for num in nums:
                if num < lowest_num:
                    lowest_num = num
            index = nums.index(lowest_num)
            nums[index] *= -1
            
            k -= 1
        
        suming = sum(nums)
        return suming