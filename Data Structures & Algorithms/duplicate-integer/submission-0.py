class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_set = set()
        for num in nums:
            if num not in empty_set:
                empty_set.add(num) 
            else:
                return True
        return False