class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
  
nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
