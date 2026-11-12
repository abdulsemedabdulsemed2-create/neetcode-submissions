class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Kmap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in Kmap:
                Kmap[nums[i]] = i
            else:
                return [Kmap[comp], i]