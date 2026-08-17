class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        max_streak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
                i += 1
            elif nums[i] == 0:
                if max_streak < cur:
                    max_streak = cur
                    cur = 0
                cur = 0
        if max_streak < cur:
                max_streak = cur
                cur = 0
        return max_streak
                
            